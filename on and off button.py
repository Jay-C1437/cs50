from Toggle import ToggleAnimator

#create an instance of the ToggleAnimator class
toggle_animator = ToggleAnimator()

#customization settings 
TYPE = 'Toothed'
COLOR = 'Dark green'
SPEED = 'Medium'

def activate_toggle():
    try:
        toggle_animator.configure(TYPE, COLOR, SPEED)
        toggle_animator.activate()
    except Exception as e:
        print(e)

#Activitae the animation
activate_toggle()        
        