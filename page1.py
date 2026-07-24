import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈Visuals")

df = pd.read_csv("cleaned.csv")

Gender_Visual = df.groupby("Churn Category")["Age"].count().reset_index().nlargest(5 , ["Age"])
# fig1 = px.bar(data_frame= Gender_Visual , x = "Age", y = "Churn Category", color = "Age")
# fig1 = px.treemap(data_frame= Gender_Visual , path = ["Churn Category"], values = "Age", color = "Age")
fig1 = px.treemap(data_frame= Gender_Visual , path = ["Churn Category"], values = "Age", title = "Churn Category Visual")
st.plotly_chart(fig1)


Offer_line_revenue = df.groupby("Monthly Charge")["Total Revenue"].count().reset_index().nlargest(10, ["Total Revenue"])
fig5 = px.area(data_frame= Offer_line_revenue , x = "Monthly Charge", y= "Total Revenue", title = "Total Charge according to Total Revenue")
st.plotly_chart(fig5)

Offer_type = df.groupby("Offer")["Customer ID"].count().reset_index()
fig2 = px.pie(data_frame= Offer_type , names = "Offer", values= "Customer ID")
st.plotly_chart(fig2)


fig12 = px.treemap(data_frame=df, path = ["City"], values = "Age")
st.plotly_chart(fig12)

# fig13 = px.imshow(df.corr(numeric_only=True),color_continuous_scale="RdBu_r", text_auto= ".1f")
fig13 = px.imshow(df.corr(numeric_only=True),color_continuous_scale="RdBu_r")
fig13.update_layout(width = 900 , height = 700)
st.plotly_chart(fig13)

# fig9 = px.scatter_3d(
#     data_frame=Offer_line_revenue,
#     x="Monthly Charge",
#     y="Total Revenue",
#     z="z"   # Replace "z" with your actual column name
# )

# st.plotly_chart(fig9)
