# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:49:20 2026

@author: nicol
"""

import re
import math
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

# -------------------- Parser for komplekse tall --------------------

def to_float(s: str) -> float:
    """Konverter streng til float, støtter både komma og punktum."""
    return float(s.replace(",", ".").strip())

def parse_polar(s: str) -> complex:
    """
    Parser polar form:
      r∠θ, r<θ, r∠θdeg, r<θdeg, r∠θrad, r<θrad
    θ i grader som standard; 'rad' = radianer.
    Eksempler: '5∠30', '8<-45deg', '2.5∠0.7rad', '1∠90°', '3,5∠10,2'
    """
    s = s.strip().lower().replace(" ", "")
    pattern = r'^([+-]?\d+(?:[.,]\d+)?)(?:∠|<)([+-]?\d+(?:[.,]\d+)?)(deg|rad|°)?$'
    m = re.match(pattern, s)
    if not m:
        raise ValueError(
            f"Ugyldig polar input: {s!r}. Bruk f.eks. 5∠30, 8<-45deg, 2.5∠0.7rad"
        )
    r_str, theta_str, unit = m.group(1), m.group(2), m.group(3)
    r = to_float(r_str)
    theta = to_float(theta_str)

    if unit in (None, "deg", "°"):
        theta_rad = math.radians(theta)
    elif unit == "rad":
        theta_rad = theta
    else:
        raise ValueError(f"Ukjent vinkel-enhet: {unit!r}")

    return complex(r * math.cos(theta_rad), r * math.sin(theta_rad))

def parse_complex(s: str, allow_blank_zero: bool = True) -> complex:
    """
    Leser både rektangulær og polar form.
    - Rektangulær: '3+2j', '-4-7j', '5', '0+1j'
    - Polar: via parse_polar (f.eks. '5∠30', '2.5<0.7rad')
    - Hvis allow_blank_zero=True: tomt felt tolkes som 0.
    """
    s = s.strip()
    if not s:
        if allow_blank_zero:
            return 0.0 + 0.0j
        raise ValueError("Tomt felt.")

    if ("∠" in s) or ("<" in s) or ("deg" in s.lower()) or ("rad" in s.lower()) or ("°" in s):
        return parse_polar(s)

    s_norm = s.replace(",", ".")
    try:
        return complex(s_norm)
    except Exception as e:
        raise ValueError(
            f"Kunne ikke tolke komplekst tall: {s!r}. Bruk f.eks. 3+2j eller 5∠30. Feil: {e}"
        )

def cmplx_to_polar_str(z: complex, nd=6) -> str:
    """Formatterer kompleks tall i polar form r∠θ°, med grader."""
    r = abs(z)
    theta = math.degrees(math.atan2(z.imag, z.real))
    if abs(r) < 10**(-nd):
        r = 0.0
    if abs(theta) < 10**(-nd):
        theta = 0.0
    return f"{r:.{nd}f}∠{theta:.{nd}f}°"

# -------------------- Scrollbar-innpakning --------------------

class ScrollFrame(ttk.Frame):
    """
    En enkel rulle-ramme med Canvas + vertikal scrollbar.
    Bruk .content for å plassere widgets.
    """
    def __init__(self, parent, height=300):
        super().__init__(parent)
        self.canvas = tk.Canvas(self, borderwidth=0, height=height)
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.content = ttk.Frame(self.canvas)
        self.content_id = self.canvas.create_window((0, 0), window=self.content, anchor="nw")

        self.content.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)

    def _on_frame_configure(self, _event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        # Strekk innholdsbredden til canvas-bredden
        canvas_width = event.width
        self.canvas.itemconfig(self.content_id, width=canvas_width)

# -------------------- GUI-app --------------------

class DetRatioGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Determinant-ratio (n×n) – rektangulær/polar input")
        self.geometry("1100x780")
        self.minsize(900, 620)

        self.n_var = tk.IntVar(value=3)
        self.allow_blank_var = tk.BooleanVar(value=True)

        self.entries_A = []
        self.entries_B = []

        self._build_ui()

    def _build_ui(self):
        # Instruksjon
        info = (
            "Skriv inn A og B (n×n). Støtter:\n"
            "  • Rektangulær: 3+2j, -1j, 5, 0.2-0.8j, 3,5+2,1j\n"
            "  • Polar: 5∠30, 8<-45deg, 2.5∠0.7rad, 1∠90°, 3,5∠10,2\n"
        )
        ttk.Label(self, text=info, justify="left").pack(padx=12, pady=(10, 6), anchor="w")

        # Toppkontroller
        top = ttk.Frame(self)
        top.pack(fill="x", padx=12, pady=6)

        ttk.Label(top, text="Størrelse n:").pack(side="left")
        self.spin_n = ttk.Spinbox(top, from_=2, to=20, width=5, textvariable=self.n_var)
        self.spin_n.pack(side="left", padx=(4, 12))
        ttk.Button(top, text="Bygg/oppdater matriser", command=self.rebuild_matrices).pack(side="left")

        ttk.Checkbutton(
            top, text="Tomme felt = 0", variable=self.allow_blank_var
        ).pack(side="left", padx=(16, 0))

        ttk.Button(top, text="Fyll eksempel", command=self.fill_example).pack(side="left", padx=8)
        ttk.Button(top, text="Tøm", command=self.clear_all).pack(side="left", padx=8)
        ttk.Button(top, text="Beregn", command=self.compute).pack(side="right")

        # Matrise-område (scrollable, side-ved-side)
        matrices_container = ttk.Frame(self)
        matrices_container.pack(fill="both", expand=True, padx=12, pady=8)

        self.frame_A = ttk.LabelFrame(matrices_container, text="Matrise A")
        self.frame_B = ttk.LabelFrame(matrices_container, text="Matrise B")
        self.frame_A.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        self.frame_B.grid(row=0, column=1, sticky="nsew", padx=(8, 0))

        matrices_container.columnconfigure(0, weight=1)
        matrices_container.columnconfigure(1, weight=1)
        matrices_container.rowconfigure(0, weight=1)

        self.scroll_A = ScrollFrame(self.frame_A, height=360)
        self.scroll_B = ScrollFrame(self.frame_B, height=360)
        self.scroll_A.pack(fill="both", expand=True, padx=6, pady=6)
        self.scroll_B.pack(fill="both", expand=True, padx=6, pady=6)

        # Resultat-seksjon
        result_frame = ttk.LabelFrame(self, text="Resultater")
        result_frame.pack(fill="both", expand=False, padx=12, pady=(0, 12))

        grid = ttk.Frame(result_frame)
        grid.pack(fill="x", padx=8, pady=8)

        self.var_detA_rect = tk.StringVar()
        self.var_detA_polar = tk.StringVar()
        self.var_detB_rect = tk.StringVar()
        self.var_detB_polar = tk.StringVar()
        self.var_ratio_rect = tk.StringVar()
        self.var_ratio_polar = tk.StringVar()
        self.var_status = tk.StringVar()

        def row(lbl, vrect, vpolar, r):
            ttk.Label(grid, text=lbl, width=18).grid(row=r, column=0, sticky="w", padx=4, pady=4)
            ttk.Entry(grid, textvariable=vrect, width=60).grid(row=r, column=1, sticky="we", padx=4, pady=4)
            ttk.Entry(grid, textvariable=vpolar, width=36).grid(row=r, column=2, sticky="we", padx=4, pady=4)

        grid.columnconfigure(1, weight=1)
        grid.columnconfigure(2, weight=1)

        row("det(A):", self.var_detA_rect, self.var_detA_polar, 0)
        row("det(B):", self.var_detB_rect, self.var_detB_polar, 1)
        row("det(A)/det(B):", self.var_ratio_rect, self.var_ratio_polar, 2)

        ttk.Label(result_frame, textvariable=self.var_status, foreground="#444").pack(anchor="w", padx=8, pady=4)

        # Bygg default 3×3
        self.rebuild_matrices()

    # -------------------- Matrise-håndtering --------------------

    def rebuild_matrices(self):
        """Re-tegn innmat i scroll-rammene basert på valgt n."""
        n = self.n_var.get()
        if n < 2 or n > 20:
            messagebox.showerror("Ugyldig n", "Størrelse n må være mellom 2 og 20.")
            return

        # Fjern gamle widgets
        for w in self.scroll_A.content.winfo_children():
            w.destroy()
        for w in self.scroll_B.content.winfo_children():
            w.destroy()

        self.entries_A = [[None]*n for _ in range(n)]
        self.entries_B = [[None]*n for _ in range(n)]

        # Lag rutene
        for i in range(n):
            for j in range(n):
                eA = ttk.Entry(self.scroll_A.content, width=16)
                eB = ttk.Entry(self.scroll_B.content, width=16)
                eA.grid(row=i, column=j, padx=4, pady=4)
                eB.grid(row=i, column=j, padx=4, pady=4)
                self.entries_A[i][j] = eA
                self.entries_B[i][j] = eB

        self.var_status.set(f"Bygget {n}×{n} matriser. Tomme felt tolkes som 0: {'Ja' if self.allow_blank_var.get() else 'Nei'}.")

    def clear_all(self):
        for entries in (self.entries_A, self.entries_B):
            for row in entries:
                for e in row:
                    e.delete(0, tk.END)
        self.var_detA_rect.set("")
        self.var_detA_polar.set("")
        self.var_detB_rect.set("")
        self.var_detB_polar.set("")
        self.var_ratio_rect.set("")
        self.var_ratio_polar.set("")
        self.var_status.set("Tømt.")

    def fill_example(self):
        """
        Fyller et ikke-singulært eksempel som skalerer med n.
        - Diagonal: 1 + j*(i+1)
        - Over-diagonal: små reelle
        - Under-diagonal: små polare
        """
        self.clear_all()
        n = self.n_var.get()
        for i in range(n):
            for j in range(n):
                eA = self.entries_A[i][j]
                eB = self.entries_B[i][j]
                if i == j:
                    # Diagonal - rektangulær
                    eA.insert(0, f"{1 + (i+1)}+{(i+1)}j")   # (2+i)+(i)j
                    eB.insert(0, f"{2 + (i+1)}+{(i+2)}j")   # (3+i)+(i+1)j
                elif j == i+1:
                    # over-diagonal - små reelle
                    eA.insert(0, f"{0.2*(i+1):.2f}")
                    eB.insert(0, f"{0.3*(i+1):.2f}")
                elif i == j+1:
                    # under-diagonal - polare
                    eA.insert(0, f"0.5∠{15*(i+1)}")
                    eB.insert(0, f"0.6∠{10*(i+1)}")
                else:
                    # annet - legg 0
                    eA.insert(0, "0")
                    eB.insert(0, "0")

        self.var_status.set("Eksempel fylt.")

    def read_matrix(self, entries):
        n = len(entries)
        M = np.zeros((n, n), dtype=complex)
        allow_blank = self.allow_blank_var.get()
        for i in range(n):
            for j in range(n):
                s = entries[i][j].get()
                M[i, j] = parse_complex(s, allow_blank_zero=allow_blank)
        return M

    # -------------------- Beregning --------------------

    def compute(self):
        try:
            A = self.read_matrix(self.entries_A)
            B = self.read_matrix(self.entries_B)

            # Determinanter
            detA = np.linalg.det(A)
            detB = np.linalg.det(B)

            # Robust nær-null sjekk
            if np.isclose(detB.real, 0.0, atol=1e-12) and np.isclose(detB.imag, 0.0, atol=1e-12):
                raise ZeroDivisionError("Determinanten til matrise B er (nær) 0 – kan ikke dele på 0.")

            ratio = detA / detB

            # Utskrift
            self.var_detA_rect.set(f"{detA.real:.8f} {'+' if detA.imag>=0 else '-'} {abs(detA.imag):.8f}j")
            self.var_detA_polar.set(cmplx_to_polar_str(detA, nd=6))
            self.var_detB_rect.set(f"{detB.real:.8f} {'+' if detB.imag>=0 else '-'} {abs(detB.imag):.8f}j")
            self.var_detB_polar.set(cmplx_to_polar_str(detB, nd=6))
            self.var_ratio_rect.set(f"{ratio.real:.8f} {'+' if ratio.imag>=0 else '-'} {abs(ratio.imag):.8f}j")
            self.var_ratio_polar.set(cmplx_to_polar_str(ratio, nd=6))

            n = self.n_var.get()
            self.var_status.set(f"Beregnet OK for {n}×{n}.")

        except ZeroDivisionError as zde:
            messagebox.showerror("Feil", str(zde))
            self.var_status.set("Feil: determinanten til B er (nær) 0.")
        except ValueError as ve:
            messagebox.showerror("Ugyldig input", str(ve))
            self.var_status.set("Ugyldig input. Se feilmelding.")
        except Exception as e:
            messagebox.showerror("Uventet feil", str(e))
            self.var_status.set("Uventet feil – se feilmelding.")

# -------------------- main --------------------

if __name__ == "__main__":
    app = DetRatioGUI()
    app.mainloop()