import pandas as pd
import streamlit as st

st.set_page_config(page_title = "Interwaste",
				   page_icon = ":bar_chart:",
				   layout = "centered")

# df = pd.read_excel(
	# io = 'data.xlsx',
	# engine = 'openpyxl',
	# sheet_name = 'Summary LN&MG Areas',
	# usecols = 'A:M',
	# nrows = 157,
	# )

df = pd.read_csv('clean_data.csv')

# st.dataframe(df)

suburb = st.selectbox(
	'Select Area',
	options=df["Suburb"]
	)

# st.write('You selected:', option)

df_selected = df.query(
	"Suburb == @suburb"
	)

area = df_selected['Area'].tolist()[0]
mon = 'Monday' if df_selected['MONDAY'].tolist()[0] else ''
tue = 'Tuesday' if df_selected['TUESDAY'].tolist()[0] else ''
wed = 'Wednesday' if df_selected['WEDNESDAY'].tolist()[0] else ''
thu = 'Thursday' if df_selected['THURSDAY'].tolist()[0] else ''
fri = 'Friday' if df_selected['FRIDAY'].tolist()[0] else ''
frequency = df_selected['Frequency'].tolist()[0]

day_of_the_week = "Day of the week: " + mon + " " + tue + " " + wed + " " + thu + " " + fri
	# 'Area',
	# 'MONDAY',
	# 'TUESDAY',
	# 'WEDNESDAY',
	# 'THURSDAY',
	# 'FRIDAY',
	# 'Frequency'].tolist()

st.write('You selected: ', suburb)
st.write('Area: ', area)
# st.write('Day of the week: ', mon, tue, wed, thu, fri)
st.write(day_of_the_week)
st.write('Frequency: ', frequency)