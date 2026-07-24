import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu 
# import pathlib
st.set_page_config(
    page_title="Customer Churn",
    page_icon="🙎‍♂️",
    layout= "wide"
)

with st.sidebar:
    opt = option_menu("Menu",options = ["Overview", "Dataset","Visuals", "Filter","About"], icons=["house","file-text","activity","bar-chart","person"],default_index=0)

# if opt == "Overview":
    # st.write("Hello World")
df = pd.read_csv("cleaned.csv")

st.sidebar.header("🔍Churn Filter")

churn = st.sidebar.multiselect(
    "Select Churn as per City",
    options=df["City"].unique(),
    default=df["City"].unique()[:3]
)
# if opt == "Filter":
#     churn = st.multiselect(
#         "Select Churn as per City",
#         options=df["City"].unique(),
#         default=df["City"].unique()[:3]
#     )


# def load_css(file_path):
#     with open(file_path) as f:
#         st.html(f"<style>{f.read()}</style>")

# css_path = pathlib.Path("customer churn PythonDS project/style.css")

st.html("style.css")

st.markdown(
    '<h1 class = "title">📊Executive Overview</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<br>',
    unsafe_allow_html=True
)

# st.title("📊Executive Overview")
# st.sidebar.success("Select a page above.")
# st.sidebar.success("Overview")
# st.sidebar.success("Visuals")

# st.sidebar.success("Gender")
# st.sidebar.success("State")
# st.sidebar.success("City")
# st.sidebar.success("Contract")
# st.sidebar.success("Customer Status")

# st.write("Objective: Provide an overall snapshot of the customer base, churn, and revenue.")
# btn = st.button("Click for Dataset", key = "green")
# if btn:
#     st.subheader("Dataset")
#     st.dataframe(df)

# st.html("style.css")

st.markdown(
    # '<div class="custom-text-box">This text has a blue background and border.</div>', 
    '<div class="custom-text-box">🎯Objective: Provide an overall snapshot of the customer base, churn, and revenue.</div>', 
    unsafe_allow_html=True
)

# # 2. Target your custom class with CSS
# st.html("""
# <style>
#     .custom-text-box {
#         background-color: #E8F0FE;
#         border: 2px solid #1A73E8;
#         padding: 10px;
#         border-radius: 5px;
#     }
# </style>
# """)

st.subheader("Dataset")
st.dataframe(df)

# st.html("style.css")
# st.button("snow", key = "red")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total Revenue", df["Total Revenue"].sum())

with c2:
    st.metric("No of customers", df["Customer ID"].nunique())
# st.write(df["Category_Offer"])
with c3:
    # st.metric("Churned Customers", ["Customer Status"].nunique())
    st.metric("no. of city", df["City"].nunique())

with c4:
    # st.metric("Under 30 Age", df["Under 30"].count())
    st.metric("No. of Offers", df["Offer"].nunique())
    
# c5, c6, c7, c8 = st.columns(4)

# with c5:
#     st.metric("")


# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""

# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)

# visuals---->
# Gender_Visual = df.groupby("Age")["Churn Category"].sum().reset_index().nlargest(5 , ["Age"])
# ---->Gender_Visual = df.groupby("Churn Category")["Age"].count().reset_index().nlargest(5 , ["Age"])
# st.dataframe(Gender_Visual)
# ---->fig1 = px.bar(data_frame= Gender_Visual , x = "Age", y = "Churn Category", color = "Age")
# ---->st.plotly_chart(fig1)
# st.header("HEllo CODe")

# fig1 = px.pie(data_frame= df , names = "Churn Category", values = "Age", color = "Churn Category", title = "Churn Category as per Age")
# st.plotly_chart(fig1)

customer_id = df.groupby("Churn Category")["Customer ID"].count().reset_index()
fig1 = px.treemap(data_frame= customer_id , path = ["Churn Category"], values = "Customer ID", color = "Churn Category", title = "Churn Category as per Age")
st.plotly_chart(fig1)

# fig1 = px.line(data_frame= df , x = "Customer ID", color = "Gender", title = "Customer Id as per ")
# fig1 = px.line(data_frame= df , x = "Customer ID", color = "Gender", title = "Customer Id as per ")
# st.plotly_chart(fig1)

Offer_type = df.groupby("Offer")["Customer ID"].count().reset_index()
fig2 = px.pie(data_frame= Offer_type , names = "Offer", values= "Customer ID", title = "Types Of Offers")
st.plotly_chart(fig2)


# print("Offer_type")

# Offer_line = df.groupby("Payment Method")["Customer ID"].count().reset_index()
# fig3 = px.line(data_frame= Offer_line , x = "Payment Method", y= "Customer ID", title = "Payment Method as per Customer ID")
# st.plotly_chart(fig3)

Offer_line = df.groupby("Payment Method")["Customer ID"].count().reset_index()
fig3 = px.bar(data_frame= Offer_line , x = "Payment Method", y= "Customer ID", color = "Payment Method",title = "Payment Method as per Customer ID")
st.plotly_chart(fig3)

df["Monthly Charge Category"] = pd.cut(
    df["Monthly Charge"],
    bins=[0, 30, 60, 90, 120],
    labels=["0-30", "31-60", "61-90", "91-120"]
)

Offer_line_revenue = (
    df.groupby("Monthly Charge Category")["Customer ID"]
      .count()
      .reset_index()
)

fig4 = px.line(
    Offer_line_revenue,
    x="Monthly Charge Category",
    y="Customer ID",
    markers=True,
    title="Customer Count by Monthly Charge Category"
)

st.plotly_chart(fig4, use_container_width=True)

# print("Offer_line_revenue")

# pd.cut
Offer_line_revenue = df.groupby("Monthly Charge")["Total Revenue"].count().reset_index().nlargest(10, ["Total Revenue"])
fig5 = px.area(data_frame= Offer_line_revenue , x = "Monthly Charge", y= "Total Revenue")
st.plotly_chart(fig5)

# fig6 = px.box(data_frame= df , x = "Gender" , y = "Monthly Charge" , color= "Gender")
# ---->fig6 = px.box(data_frame= df , x = "Gender" , y = "Total Revenue" , color= "Gender")
Gender_wise_total_revenue = df.groupby("Gender")["Total Revenue"].sum().reset_index()
# st.dataframe(Gender_wise_total_revenue)
fig6 = px.pie(data_frame= Gender_wise_total_revenue , names = "Gender" , values = "Total Revenue" , color= "Gender", hole = 0.5, title = "Total Revenue as per Gender")
st.plotly_chart(fig6)

# fig7 = px.scatter(data_frame= df , x = "Total Revenue" ,y = "Monthly Charge")
# # fig7 = px.scatter(data_frame= df , x = "Total Revenue" ,y = "Total Charges")
# st.plotly_chart(fig7)

# fig8 = px.violin(data_frame= df , x = "Gender" , y = "Age" , color = "Gender")
# st.plotly_chart(fig8)


# fig9 = px.violin(data_frame= df , x = "Gender" , y = "Age", box = True , color = "Under 30")
# st.plotly_chart(fig9)
# fig9 = px.line_3d(data_frame= Offer_line_revenue , x = "Monthly Charge", y= "Total Revenue")
# fig9 = px.line_3d(data_frame= df , x = "Monthly Charge", y= "Total Revenue" , z = "z")
# st.plotly_chart(fig9)

# fig10 = px.pie(data_frame= df , names= "Gender" , values= "Age" , hole = 0.5)
# st.plotly_chart(fig10)

# fig11 = px.treemap(data_frame=df, path = ["Gender"], values = "Age")
# st.plotly_chart(fig11)

# fig12 = px.treemap(data_frame=df, path = ["City"], values = "Age", color = "Gender")

# city_wise_total_revenue = df.groupby("City")["Total Revenue"].max().reset_index().nlargest(10, ["Total Revenue"])

# fig12 = px.pie(data_frame=city_wise_total_revenue, names= "Citystyle", values = "Total Revenue")
# st.plotly_chart(fig12)

city_wise_total_revenue = (
    df.groupby("City")["Total Revenue"]
      .sum()
      .reset_index()
      .sort_values("Total Revenue")
      .nlargest(10, "Total Revenue")
)

fig12 = px.bar(
    city_wise_total_revenue,
    x="Total Revenue",
    y="City",
    orientation="h",
    color="Total Revenue",
    title="Top 10 Cities by Total Revenue"
)

st.plotly_chart(fig12, use_container_width=True)

# fig13 = px.imshow(df.corr(numeric_only=True))
# st.plotly_chart(fig13)

fig13 = px.imshow(df.corr(numeric_only=True) , text_auto= True, title = "HeatMap")
fig13.update_layout(width = 500, height = 700)
st.plotly_chart(fig13)

# fig14 = px.bar(data_frame= df, x = "Customer Status" , y = "Total Revenue", color = "Gender")
fig14 = px.bar(data_frame= df, x = "Customer Status" , y = "Total Revenue" , color = "Customer Status")
st.plotly_chart(fig14)

fig15 = px.histogram(data_frame=df, x = "Monthly Charge", nbins = 30)
st.plotly_chart(fig15)

fig16 = px.histogram(data_frame=df, x = "Total Revenue", nbins = 25)
st.plotly_chart(fig16)

# fig17 = px.scatter(data_frame=df, x = "Monthly Charge", y = "Total Revenue")
# fig17 = px.scatter(data_frame=df, x = "Monthly Charge", y = "Total Revenue", color = "Total Revenue")
fig17 = px.box(data_frame=df, x = "Monthly Charge Category", y = "Total Revenue", color = "Monthly Charge Category", title = "Revenue by Monthly Charge Category")
st.plotly_chart(fig17)

# fig18 = px.box(data_frame=df, x = "Customer Status", y = "Satisfaction Score", color = "Customer Status")
# st.plotly_chart(fig18)

df["Satisfaction Level"] = pd.cut(
    df["Satisfaction Score"],
    bins=[0, 2, 4, 5],
    labels=["Low", "Medium", "High"]
)
fig18 = px.bar(
    df,
    x="Satisfaction Level",
    y="Monthly Charge",
    color="Satisfaction Level",
    title="Monthly Charge by Satisfaction Level"
)

st.plotly_chart(fig18, use_container_width=True)