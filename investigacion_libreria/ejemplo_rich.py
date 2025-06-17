from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Ventas Mensuales")

table.add_column("Mes", style="cyan", no_wrap=True)
table.add_column("Producto", style="magenta")
table.add_column("Ingresos", justify="right", style="green")

table.add_row("Enero", "Zapatos", "$5000")
table.add_row("Febrero", "Camisetas", "$4200")
table.add_row("Marzo", "Pantalones", "$6100")

console.print(table)