# Tableau Tips

## How to determine where a parameter is used

To determine where a parameter is used, attempt to delete it.

A confirmation dialog box appears that lists the affected fields and sheets.

**Note**: If the parameter is used in a customer SQL query, it will not be listed in the dialog box.

Source: [Tracing Parameter used in tableau](https://community.tableau.com/s/question/0D54T00000C68BJSAZ/tracing-parameter-used-in-tableau)

## How to create a donut chart with two labels

1. Create a normal pie chart (adding labels as necessary)
1. Select pie from Marks drop-down
1. Add dimension to color
1. Add measure to angle
1. Add labels as necessary
1. Create calculation: MIN(0)
1. Add the calculation twice to rows, and select Dual Axis.
1. In the second instance in the Marks card, remove all the values, change color to white, and decrease the size. (This is the donut hole. :-)) 
1. Increase the size of the first instance of the calculation as necessary.
