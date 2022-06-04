import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
#    ['ping', '127.0.0.1', '-c', '4'],
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
)

saida = proc.stdout
saida = saida.replace('TTL', 'FOI_TTL')
print(saida)
