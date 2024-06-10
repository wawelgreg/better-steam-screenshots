import logging as log

# Logger configuration
FORMAT = '%(asctime)s|%(levelname)s|%(message)s'
log.basicConfig(filename='bss.log', format=FORMAT, level=log.INFO)