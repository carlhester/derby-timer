# bootstrap

# database
import Databaser
DB = Databaser.Databaser()
execfile("schema.py")

import Randomizer
RND = Randomizer.Randomizer()

execfile("seed.py")

# admin interface

# presentation


