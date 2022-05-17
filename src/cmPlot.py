from matplotlib.pyplot import plot, show
import PySimpleGUI as sg
import utils

sg.theme('Dark Blue 3')   # Add a touch of color



# All the stuff inside your window.
layout = [[sg.Text('Function'), sg.InputText(key='-FUNC-')],
          [sg.Text('Minimum Value'), sg.InputText(size=(5, 1), key='-MIN-'),
           sg.Text('Maximum Value'), sg.InputText(size=(5, 1), key='-MAX-')],
          [sg.Canvas(key='-CANVAS-')],
          [sg.Button('Plot')]]


# Create the Window
window = sg.Window('cmPlot', layout, resizable=True, finalize=True)

# Close the window when the escape key is pressed
window.bind('<Escape>', '-ESC-')

# Event Loop to process "events" and get the "values" of the inputs


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel', '-ESC-'):  # if user closes window or clicks cancel
        break
    elif event == 'Plot':
        success, output = utils.get_x_y_vals(values['-FUNC-'], values['-MIN-'], values['-MAX-'])
        if success == True:
            plot(output[0], output[1])
            show(block=True)
        else:
            sg.popup(utils.getErrorMsg(output), title='Error', keep_on_top=True)

window.close()

