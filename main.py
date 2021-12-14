from UI.consola import run_console
from Tests.run_all_tests import run_all_tests
from Domain.aeroport import create_aeroport

def main():
    aeroport = create_aeroport()
    run_console(aeroport)

run_all_tests()
main()
