"""Mainly for use when the database has been deleted:)"""

import models


#add some job categories
for category in ("Purchase", "Repair", "Decorate", "Clean"):
    models.Category.create(name=category).save()

for room in ("Cellar", "Kitchen", "Dining Room", "Living Room",  "Lower Stairs", "Upper Stairs", "Garden", "Landing", "Evelyn's Room", "Nanu Room", "Bathroom", "Bassoon Room", "Our Room", "Outside", "Elsewhere"):
    models.Room.create(name=room).save()
    
