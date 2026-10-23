import click
from pathlib import Path

@click.group()
@click.version_option(version="0.1.0", prog_name="StegaTools")
def cli():
    """StegaTools - Mini multiherramienta de esteganografía educativa."""
    pass

@cli.command()
@click.argument('carrier_path', type=click.Path(exists=True))
@click.argument('payload_file', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.option('--mode', '-m', 
              type=click.Choice(['meta', 'lsb', 'unicode']),
              required=True,
              help='Técnica de esteganografía a utilizar.')
def embed(carrier_path, payload_file, output_path, mode):
    """Incrusta un archivo en un portador usando la técnica especificada."""
    # Leer payload
    payload = Path(payload_file).read_bytes()
    
    # Importar dinámicamente el módulo correcto
    if mode == 'meta':
        from stegatools.meta import embed as embed_func
        embed_func(str(carrier_path), payload, str(output_path))
    elif mode == 'lsb':
        from stegatools.lsb import embed as embed_func
        embed_func(str(carrier_path), payload, str(output_path))
    elif mode == 'unicode':
        from stegatools.ununicode import embed as embed_func
        # Nota: para unicode el portador es texto, no archivo binario
        carrier_text = Path(carrier_path).read_text()
        result = embed_func(carrier_text, payload)
        Path(output_path).write_text(result)

@cli.command()
@click.argument('carrier_path', type=click.Path(exists=True))
@click.option('--mode', '-m',
              type=click.Choice(['meta', 'lsb', 'unicode']),
              required=True)
def extract(carrier_path, mode):
    """Extrae el payload oculto de un portador."""
    if mode == 'meta':
        from stegatools.meta import extract as extract_func
        result = extract_func(str(carrier_path))
    elif mode == 'lsb':
        from stegatools.lsb import extract as extract_func
        result = extract_func(str(carrier_path))
    elif mode == 'unicode':
        from stegatools.ununicode import extract as extract_func
        text = Path(carrier_path).read_text()
        result = extract_func(text)
    
    if result:
        click.echo(f"Payload extraído ({len(result)} bytes)")
        click.echo(result.decode('utf-8', errors='replace'))
    else:
        click.echo("No se encontró ningún payload.")

@cli.command()
@click.argument('carrier_path', type=click.Path(exists=True))
@click.option('--mode', '-m',
              type=click.Choice(['meta', 'lsb', 'unicode']),
              required=True)
def detect(carrier_path, mode):
    """Detecta si un portador contiene datos ocultos."""
    if mode == 'meta':
        from stegatools.meta import detect as detect_func
        result = detect_func(str(carrier_path))
    elif mode == 'lsb':
        from stegatools.lsb import detect as detect_func
        result = detect_func(str(carrier_path))
    elif mode == 'unicode':
        from stegatools.ununicode import detect as detect_func
        text = Path(carrier_path).read_text()
        result = detect_func(text)
    
    status = "✓ Sospecha de payload oculto" if result else "✗ No se detectó nada"
    click.echo(f"[{mode.upper()}] {status}")

@cli.command()
@click.argument('carrier_path', type=click.Path(exists=True))
@click.option('--mode', '-m',
              type=click.Choice(['meta', 'lsb', 'unicode']),
              required=True)
def capacity(carrier_path, mode):
    """Muestra la capacidad máxima de un portador."""
    if mode == 'meta':
        from stegatools.meta import capacity as cap_func
    elif mode == 'lsb':
        from stegatools.lsb import capacity as cap_func
    elif mode == 'unicode':
        click.echo("Capacidad ilimitada (depende del texto)")
        return
    else:
        return
    
    cap = cap_func(str(carrier_path))
    click.echo(f"Capacidad máxima: {cap} bytes ({cap / 1024:.2f} KB)")

if __name__ == '__main__':
    cli()
