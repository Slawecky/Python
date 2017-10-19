import io
from contextlib import redirect_stdout

def get_print_output(testowan_funkcja):
    bufor_pamieci = io.StringIO()
    with redirect_stdout (bufor_pamieci):

