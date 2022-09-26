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

df = pd.read_csv('data-service-v01.csv')

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

cols = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
sd_by_cols = df_selected[df_selected.columns[cols]]
sd_by_cols_to_list = sd_by_cols.values.tolist()

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
# st.write(sd_by_cols["SD01"])
st.write('Next Service: ', sd_by_cols_to_list)

# if sd_by_cols[sd_by_cols["SD01"].isnull().any()]:
	# print(sd_by_cols["SD01"])	
	# st.write('Next Service: ', sd_by_cols["SD01"])