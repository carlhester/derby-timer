# bootstrap

# database
import Databaser
DB = Databaser.Databaser()
execfile("schema.py")

import Randomizer
RND = Randomizer.Randomizer()

execfile("seed.py")

import Outputter
OUT = Outputter.Outputter()

OUT.writeToTemplate(0, "test", "output")
# admin interface

# presentation


