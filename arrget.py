#!/usr/bin/env python3
from pycliarr.api import RadarrCli
apikey = "7868d511ec6b4524af4f29202b68ab69"
radarr_cli = RadarrCli('http://localhost:7878', apikey)
radarr_cli.add_movie(imdb_id="6320628", quality=1)
#movie = radarr_cli.get_movie(12)
