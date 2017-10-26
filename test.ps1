$movementRequests=@(@{direction='left';distance=3})
iwr http://localhost:5000/move -Method post -ContentType 'application/json' -Body ($movementRequests|ConvertTo-Json -Depth 100)
