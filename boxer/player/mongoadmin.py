# myapp/mongoadmin.py

# Import the MongoAdmin base class
from mongonaut.sites import MongoAdmin

# Import your custom models
from player.documents import Player

# Instantiate the MongoAdmin class
# Then attach the mongoadmin to your model
Player.mongoadmin = MongoAdmin()