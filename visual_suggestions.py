import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("cleaned.csv")

st.title("More Visuals")

fig1 = px.pie(data_frame=df, names = "Customer Status", title = "Customer Status Distribution")
st.plotly_chart(fig1)

fig2 = px.pie(data_frame=df, names = "Churn Label", title = "Churn VS Non-Churn")
st.plotly_chart(fig2)

gender_churn = df.groupby(["Gender", "Churn Label"]).size().reset_index(name = "Count")
fig3 = px.bar(data_frame=gender_churn, x = "Gender", y = "Count", color = "Churn Label",barmode= "group",title = "Gender VS Churn")
st.plotly_chart(fig3)

fig4 = px.histogram(data_frame=df , x = "Age", nbins = 25, color = "Churn Label",title = "Age Distribution")
st.plotly_chart(fig4)

fig5 = px.histogram(data_frame=df , x = "Monthly Charge", nbins = 25, color = "Churn Label",title = "Age Distribution")
fig5 = px.histogram(data_frame=df , x = "Monthly Charge", marginal= "box", color = "Churn Label",title = "Monthly Charge Distribution")
st.plotly_chart(fig5)

fig6 = px.scatter(data_frame=df , x = "Monthly Charge", y = "Total Revenue", color = "Churn Label", hover_data= ["Customer ID"],title = "Monthly Charge VS Total Revenue")
st.plotly_chart(fig6)

contract_churn = df.groupby(["Contract", "Churn Label"]).size().reset_index(name = "Count")
fig7 = px.bar(data_frame=contract_churn, x = "Contract", y = "Count", color = "Churn Label",barmode= "group",title = "Contract Type VS Churn")
st.plotly_chart(fig7)

fig8 = px.bar(df["Internet Type"].value_counts().reset_index(), x = "Internet Type", y = "count", color = "Internet Type",title = "Internet Type Distribution")
st.plotly_chart(fig8)

churn_internet_type = df.groupby(["Internet Type", "Churn Label"]).size().reset_index(name = "Count")
fig9 = px.bar(data_frame=churn_internet_type,x = "Internet Type", y = "Count", color = "Churn Label",barmode= "group",title = "Churn By Internet Type")
st.plotly_chart(fig9)

payment_method = df.groupby(["Payment Method" ,"Churn Label"]).size().reset_index(name = "Count")
fig10 = px.bar(data_frame=payment_method, x = "Payment Method", y = "Count", color = "Churn Label", barmode= "group",title = "Payment Method VS Churn")
st.plotly_chart(fig10)

offer_analysis = df.groupby(["Offer", "Churn Label"]).size().reset_index(name = "Count")
# fig11 = px.bar(data_frame=offer_analysis, x = "Offer", y = "Count", color = "Offer",title = "Offer VS Churn")
fig11 = px.bar(data_frame=offer_analysis, x = "Offer", y = "Count", color = "Churn Label", barmode= "group",title = "Offer VS Churn")
st.plotly_chart(fig11)

# fig12 = px.box(data_frame=df, x = "Churn Label", y = "Satisfaction Score", color = "Satisfaction Score", title = "Satisfaction Score VS Churn")
fig12 = px.box(data_frame=df, x = "Churn Label", y = "Satisfaction Score", color = "Churn Label", title = "Satisfaction Score VS Churn")
st.plotly_chart(fig12)

fig13 = px.bar(df["Churn Category"].value_counts().reset_index(), x="Churn Category", y="count", color = "Churn Category",title = "Churn Categories")
st.plotly_chart(fig13)
 
top_churn_reason = df["Churn Reason"].value_counts().head(10) 
 
fig14 = px.bar(data_frame = top_churn_reason.reset_index(), x="Churn Reason", y="count", color = "Churn Reason",title="Top 10 Churn Reasons")
st.plotly_chart(fig14)

# state = df.groupby("State").size().reset_index(name="Customers") 
# fig15 = px.choropleth(data_frame = state, locations="State", locationmode="USA-states",color="Customers",scope="usa",title="Customers by State")
# st.plotly_chart(fig15)

fig16 = px.histogram(data_frame = df, x="Tenure in Months", color="Churn Label", title="Tenure Distribution")
st.plotly_chart(fig16)

customer_status_total_revenue = df.groupby("Customer Status")["Total Revenue"].sum().reset_index()
fig17 = px.bar(data_frame = customer_status_total_revenue, x="Customer Status", y="Total Revenue", color="Customer Status", title="Revenue by Customer Status")
st.plotly_chart(fig17)

fig18 = px.box(data_frame = df, x="Churn Label", y="CLTV", color="Churn Label", title="Customer Lifetime Value")
st.plotly_chart(fig18)
 
num = df.select_dtypes(include="number")
fig19 = px.imshow(num.corr(), text_auto=True, title="Correlation Heatmap")
st.plotly_chart(fig19)

fig20 = px.scatter_mapbox( data_frame = df, lat="Latitude", lon="Longitude", color="Churn Label", hover_name="City", zoom=3, mapbox_style="carto-positron", title="Customer Locations")
st.plotly_chart(fig20)