"""Mainly for use when the database has been deleted:)"""

import models

#add some job categories
for category in ("Purchase", "Repair", "Decorate", "Clean"):
    models.Category.create(name=category).save()
    
