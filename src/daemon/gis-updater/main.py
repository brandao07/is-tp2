import sys
import time

POLLING_FREQ = int(sys.argv[1]) if len(sys.argv) >= 2 else 60
ENTITIES_PER_ITERATION = int(sys.argv[2]) if len(sys.argv) >= 3 else 10

if __name__ == "__main__":

    while True:
        print(f"Getting up to {ENTITIES_PER_ITERATION} entities without coordinates...")
        # TODO: Fazer um GET a entities API a procura dos paises sem coordenadas
        # TODO: Apos o GET adicionar coordenadas com o API que estamos a usar no importer
        # TODO: Apos inserir as coordenadas mandar de volta para o entities API que vai adicionar na bd
        time.sleep(POLLING_FREQ)
