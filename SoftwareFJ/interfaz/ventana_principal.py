import tkinter as tk
from tkinter import messagebox

from modelos.cliente import Cliente
from modelos.reserva import Reserva

from modelos.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from utils.logger import registrar_log


class VentanaPrincipal:

    def __init__(self, root):
        self.root = root
        self.root.title("Software FJ")
        self.root.geometry("1200x700")
        self.root.config(bg="#F4F4F4")

        self.COLOR_PRIMARIO = "#5B2C83"
        self.COLOR_SECUNDARIO = "#3A1B52"
        self.COLOR_FONDO = "#F4F4F4"
        self.COLOR_BLANCO = "#FFFFFF"
        self.COLOR_NEGRO = "#1E1E1E"

        self.clientes = []
        self.servicios = []
        self.reservas = []

        self.crear_interfaz()

    # ================= UI =================

    def crear_interfaz(self):
        encabezado = tk.Frame(self.root, bg=self.COLOR_SECUNDARIO, height=90)
        encabezado.pack(fill="x")

        tk.Label(encabezado, text="SOFTWARE FJ",
                 bg=self.COLOR_SECUNDARIO,
                 fg=self.COLOR_BLANCO,
                 font=("Segoe UI", 22, "bold")).pack(pady=(15, 0))

        contenedor = tk.Frame(self.root, bg=self.COLOR_FONDO)
        contenedor.pack(fill="both", expand=True)

        menu = tk.Frame(contenedor, bg=self.COLOR_PRIMARIO, width=250)
        menu.pack(side="left", fill="y")

        self.panel = tk.Frame(contenedor, bg=self.COLOR_FONDO)
        self.panel.pack(side="right", fill="both", expand=True)

        botones = [
            ("Registrar Cliente", self.formulario_cliente),
            ("Ver Clientes", self.ver_clientes),
            ("Crear Servicio", self.formulario_servicio),
            ("Ver Servicios", self.ver_servicios),
            ("Crear Reserva", self.formulario_reserva),
            ("Ver Reservas", self.ver_reservas),
            ("Simular", self.simular_operaciones),
            ("Salir", self.root.quit)
        ]

        for t, c in botones:
            tk.Button(menu, text=t, command=c,
                      bg=self.COLOR_SECUNDARIO,
                      fg=self.COLOR_BLANCO,
                      font=("Segoe UI", 11, "bold"),
                      relief="flat",
                      padx=20,
                      pady=15).pack(fill="x", padx=15, pady=10)

        self.pantalla_inicio()

    # ================= UTIL =================

    def limpiar_panel(self):
        for w in self.panel.winfo_children():
            w.destroy()

    def pantalla_inicio(self):
        self.limpiar_panel()
        tk.Label(self.panel,
                 text="Sistema listo para operar",
                 bg=self.COLOR_FONDO,
                 fg=self.COLOR_NEGRO,
                 font=("Segoe UI", 24, "bold")).pack(pady=60)

    # ================= CLIENTES =================

    def formulario_cliente(self):
        self.limpiar_panel()

        tk.Label(self.panel, text="Registro de Clientes",
                 font=("Segoe UI", 18, "bold")).pack(pady=10)

        frame = tk.Frame(self.panel, bg=self.COLOR_FONDO)
        frame.pack(pady=10)

        tk.Label(frame, text="Nombre").grid(row=0, column=0, sticky="w")
        nombre = tk.Entry(frame, width=30)
        nombre.grid(row=0, column=1)

        # CORREGIDO: Ahora pide Correo en lugar de Documento
        tk.Label(frame, text="Correo").grid(row=1, column=0, sticky="w")
        correo = tk.Entry(frame, width=30)
        correo.grid(row=1, column=1)

        tk.Label(frame, text="Teléfono").grid(row=2, column=0, sticky="w")
        telefono = tk.Entry(frame, width=30)
        telefono.grid(row=2, column=1)

        def guardar():
            n = nombre.get().strip()
            c = correo.get().strip()
            t = telefono.get().strip()

            if not n or not c or not t:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            try:
                # CORREGIDO: Se pasa (nombre, correo, telefono) al modelo Cliente
                cliente = Cliente(n, c, t)
                self.clientes.append(cliente)

                registrar_log(f"Cliente creado: {n}")
                messagebox.showinfo("OK", "Cliente registrado")

                nombre.delete(0, tk.END)
                correo.delete(0, tk.END)
                telefono.delete(0, tk.END)

            except Exception as e:
                registrar_log(f"ERROR cliente: {e}")
                messagebox.showerror("Error", str(e))

        tk.Button(self.panel, text="Guardar", command=guardar).pack(pady=10)

    def ver_clientes(self):
        self.limpiar_panel()

        tk.Label(self.panel, text="Clientes",
                 font=("Segoe UI", 18, "bold")).pack(pady=10)

        if not self.clientes:
            tk.Label(self.panel, text="Sin clientes").pack()
            return

        for c in self.clientes:
            # CORREGIDO: Se utilizan los métodos 'get' del encapsulamiento
            tk.Label(self.panel,
                     text=f"{c.get_nombre()} | {c.get_correo()} | {c.get_telefono()}",
                     anchor="w").pack(fill="x")

    # ================= SERVICIOS =================

    def formulario_servicio(self):
        self.limpiar_panel()

        tk.Label(self.panel, text="Crear Servicio",
                 font=("Segoe UI", 18, "bold")).pack(pady=10)

        tipo = tk.StringVar(value="Sala")
        costo = tk.Entry(self.panel)

        tk.Label(self.panel, text="Tipo").pack()
        tk.OptionMenu(self.panel, tipo,
                      "Sala", "Equipo", "Asesoria").pack()

        tk.Label(self.panel, text="Costo base").pack()
        costo.pack()

        def crear():
            try:
                valor = float(costo.get())

                if tipo.get() == "Sala":
                    servicio = ReservaSala()
                elif tipo.get() == "Equipo":
                    servicio = AlquilerEquipo()
                else:
                    servicio = AsesoriaEspecializada()

                servicio.costo = valor
                self.servicios.append(servicio)

                registrar_log(f"Servicio creado: {tipo.get()}")

                messagebox.showinfo("OK", "Servicio creado")

                costo.delete(0, tk.END)

            except ValueError:
                registrar_log("ERROR servicio: costo inválido")
                messagebox.showerror("Error", "Costo inválido")

        tk.Button(self.panel, text="Crear", command=crear).pack(pady=10)

    def ver_servicios(self):
        self.limpiar_panel()

        tk.Label(self.panel, text="Servicios",
                 font=("Segoe UI", 18, "bold")).pack(pady=10)

        if not self.servicios:
            tk.Label(self.panel, text="Sin servicios").pack()
            return

        for s in self.servicios:
            tk.Label(self.panel,
                     text=f"{type(s).__name__} - {getattr(s,'costo',0)}"
                     ).pack()

    # ================= RESERVAS =================

    def formulario_reserva(self):
        self.limpiar_panel()

        tk.Label(self.panel, text="Crear Reserva",
                 font=("Segoe UI", 18, "bold")).pack(pady=10)

        if not self.clientes or not self.servicios:
            tk.Label(self.panel, text="Faltan clientes o servicios").pack()
            return

        cliente_var = tk.StringVar()
        servicio_var = tk.StringVar()
        horas = tk.Entry(self.panel)

        tk.Label(self.panel, text="Cliente").pack()
        # CORREGIDO: Utiliza c.get_nombre()
        tk.OptionMenu(self.panel, cliente_var,
                      *[c.get_nombre() for c in self.clientes]).pack()

        tk.Label(self.panel, text="Servicio").pack()
        tk.OptionMenu(self.panel, servicio_var,
                      *[type(s).__name__ for s in self.servicios]).pack()

        tk.Label(self.panel, text="Horas").pack()
        horas.pack()

        def crear():
            try:
                h = int(horas.get())

                # CORREGIDO: Utiliza c.get_nombre()
                cliente = next(c for c in self.clientes if c.get_nombre() == cliente_var.get())

                servicio = self.servicios[
                    [type(s).__name__ for s in self.servicios].index(servicio_var.get())
                ]

                total = getattr(servicio, "costo", 0) * h

                reserva = Reserva(cliente, servicio)
                reserva.total = total

                self.reservas.append(reserva)

                registrar_log(f"Reserva creada {total}")

                messagebox.showinfo("OK", f"Reserva creada: {total}")

                horas.delete(0, tk.END)

            except Exception as e:
                registrar_log(f"ERROR reserva: {e}")
                messagebox.showerror("Error", "Datos inválidos")

        tk.Button(self.panel, text="Crear Reserva", command=crear).pack(pady=10)

    def ver_reservas(self):
        self.limpiar_panel()

        tk.Label(self.panel, text="Reservas",
                 font=("Segoe UI", 18, "bold")).pack(pady=10)

        if not self.reservas:
            tk.Label(self.panel, text="Sin reservas").pack()
            return

        for r in self.reservas:
            # CORREGIDO: r.cliente.get_nombre()
            tk.Label(self.panel,
                     text=f"{r.cliente.get_nombre()} -> {type(r.servicio).__name__} | {getattr(r,'total',0)}"
                     ).pack()

    # ================= SIMULACIÓN =================

    def simular_operaciones(self):
        self.limpiar_panel()

        tk.Label(self.panel,
                 text="RESULTADO SIMULACIONES",
                 font=("Segoe UI", 18, "bold")).pack(pady=10)

        salida = []

        c = None
        s = None

        try:
            # CORREGIDO: Ahora los datos coinciden con Nombre, Correo, Teléfono
            c = Cliente("Test", "test@mail.com", "3001234567")
            self.clientes.append(c)
            registrar_log("Simulación cliente")
            salida.append("OK: Cliente creado")
        except Exception as e:
            salida.append(f"ERROR cliente: {e}")

        try:
            s = ReservaSala()
            s.costo = 10000
            self.servicios.append(s)
            registrar_log("Simulación servicio")
            salida.append("OK: Servicio creado")
        except Exception as e:
            salida.append(f"ERROR servicio: {e}")

        try:
            if c is None or s is None:
                raise Exception("Dependencias incompletas")

            r = Reserva(c, s)
            r.total = s.costo * 2
            self.reservas.append(r)

            registrar_log("Simulación reserva")
            salida.append("OK: Reserva creada")

        except Exception as e:
            salida.append(f"ERROR reserva: {e}")

        try:
            Reserva(None, None)
            salida.append("ERROR no detectado")
        except Exception:
            salida.append("ERROR controlado correcto")

        txt = tk.Text(self.panel)
        txt.pack(fill="both", expand=True)

        txt.insert("1.0", "\n".join(salida))
        txt.config(state="disabled")
        