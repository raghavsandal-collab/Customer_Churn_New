import streamlit as st
import pandas as pd
import plotly.express as px
import dashboard2 as d2
import dashboard3 as d3
import dashboard4 as d4
import about as ab
from streamlit_option_menu import option_menu 
# import pathlib
st.set_page_config(
    page_title="Customer Churn",
    page_icon="🙎‍♂️",
    layout= "wide"
)

st.html("style.css")
st.markdown("""
<style>

/* ===========================
   Customer Churn Dashboard
   Sky Blue + Dark Blue Theme
   =========================== */

/* Main App */
.stApp {
    background: linear-gradient(135deg, #EAF8FF 0%, #D6F1FF 100%);
    background: linear-gradient(135deg, #EAF8FF 0%, #D6F1FF 100%);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    # background: linear-gradient(180deg, #0B3D91 0%, #1565C0 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Dashboard Title */
.title {
    color: #0B3D91;
    font-size: 40px;
    font-weight: 700;
    text-align: center;
    padding: 12px;
    background: linear-gradient(to right, #87CEEB, #D6F1FF);
    border-radius: 12px;
    border: 2px solid #1565C0;
    margin-bottom: 20px;
}

/* Objective Box */
.custom-text-box {
    background: #E3F2FD;
    color: #0B3D91;
    border-left: 8px solid #0B3D91;
    padding: 15px;
    border-radius: 10px;
    font-size: 18px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.15);
}

/* Metric Cards */
div[data-testid="metric-container"] {
    background: linear-gradient(135deg, #87CEEB, #D6F1FF);
    border: 2px solid #1565C0;
    border-radius: 15px;
    padding: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
}

div[data-testid="metric-container"] label {
    color: #0B3D91 !important;
    font-weight: bold;
}

div[data-testid="metric-container"] div {
    color: #0B3D91 !important;
}

/* Buttons */
.stButton>button {
    background-color: #1565C0;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #0B3D91;
    color: white;
}

/* Tabs */
button[data-baseweb="tab"] {
    background-color: #D6F1FF;
    color: #0B3D91;
    border-radius: 8px;
    font-weight: bold;
    margin-right: 5px;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #1565C0;
    color: white;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background: #EAF8FF;
    border-radius: 8px;
}

/* Multiselect */
.stMultiSelect div[data-baseweb="select"] {
    background: #EAF8FF;
    border-radius: 8px;
}

/* DataFrame */
div[data-testid="stDataFrame"] {
    border: 2px solid #87CEEB;
    border-radius: 10px;
}

/* Plotly Charts */
div[data-testid="stPlotlyChart"] {
    background: white;
    border-radius: 12px;
    padding: 10px;
    border: 2px solid #87CEEB;
    box-shadow: 0 3px 8px rgba(0,0,0,0.12);
}

/* Headers */
h1, h2, h3 {
    color: #0B3D91;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #D6F1FF;
}

::-webkit-scrollbar-thumb {
    background: #1565C0;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #0B3D91;
}

</style>
""", unsafe_allow_html=True)
# Define your custom background color via CSS
page_bg_css = """
<style>
# [data-testid="stAppViewContainer"] {
#     background-color: #F0F8FF;
# }
# [data-testid="stSidebar"] {
#     background-color: #151B54;
# }
</style>
"""

# Inject the CSS with unsafe_allow_html enabled
st.markdown(page_bg_css, unsafe_allow_html=True)

# st.title("My Customized App")

# st.navigation(["app", "Visuals"])
st.html("style.css")
with st.sidebar:
    opt = option_menu("Menu",options = ["Overview", "Customer Demographics & Services","Churn Analysis", "Revenue & Customer Lifetime Value","About"], icons=["house","file-text","activity","bar-chart","person"],default_index=0, key = "menu")

# if opt == "Overview":
    # st.write("Hello World")


if opt == "Overview":

    df = pd.read_csv("cleaned.csv")

    st.sidebar.header("🔍Churn Filter")

    # churn = st.sidebar.multiselect(
    #     "Select Churn as per City",
    #     options=df["City"].unique(),
    #     default=df["City"].unique()[:3]
    # )

    # churn = st.multiselect(
    #     "Select Churn as per City",
    #     options=df["City"].unique(),
    #     default=df["City"].unique()[:3]
    # )

    # df = df[(df["City"].isin(churn)) 
    # # (df["visuals"].isin(visuals)) &
    # # df(["insight"].isin())
    # ]

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

    st.sidebar.header("📊Visuals")

    visuals = st.sidebar.multiselect(
        "Select Visual",
        options=["Bar Graph", "Line Graph", "Pie Chart", "Scatter"],
        default=["Bar Graph"][:3]
    )

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
        '<div class="custom-text-box"><b>🎯Objective:</b> Provide an overall snapshot of the customer base, churn, and revenue.</div>', 
        unsafe_allow_html=True
    )

    st.markdown(
        # '<div class="custom-text-box">This text has a blue background and border.</div>', 
        '<br>', 
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

    st.sidebar.header("📊Insights")

    insight = st.sidebar.multiselect(
        "Select Insight to know",
        options=["Total No. of Customers", "Number of Offers","Churned Customers", "CLTV"],
        default=["CLTV"][:3]
    )

    tab1,tab2,tab3 =st.tabs(["Overview", "Dataset", "Visuals"])

    with tab1:

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("💵Total Revenue", round(df["Total Revenue"].sum(),2))

        with c2:
            st.metric("🙎‍♂️No of customers", df["Customer ID"].nunique())
        with c3:
            st.metric("🏙️no. of Cities", df["City"].nunique())

        with c4:
            st.metric("🎯No. of Offers", df["Offer"].nunique())

        churn = st.multiselect(
            "Select Churn as per City",
            options=df["City"].unique(),
            default=df["City"].unique()[:3]
        )

        df = df[(df["City"].isin(churn)) 
        # (df["visuals"].isin(visuals)) &
        # df(["insight"].isin())
        ]

        c1, c2 = st.columns(2)

        with c1:
            figure = px.histogram(data_frame=df, x = "Total Revenue", nbins = 25, title = "Total Revenue")
            st.plotly_chart(figure)
            contract_wise_customer = df.groupby("Contract")["Customer ID"].count().reset_index()
            figure1 = px.pie(data_frame=contract_wise_customer, names = "Contract", values= "Customer ID"  , hole= 0.5)
            st.plotly_chart(figure1)
            # customer_fig = df.groupby("Customer ID")["City"].sum().reset_index().nlargest(10,["Customer ID"])
            # figure1 = px.histogram(data_frame=df,x = "Customer ID",nbins = 5)
            # st.plotly_chart(figure1)

        total_Customer = df.groupby("Gender")["Customer ID"].count().reset_index()
        figure2 = px.pie(data_frame= total_Customer , names = "Gender" , values = "Customer ID" , color= "Gender", hole = 0.5, title = "Customer ID as per Gender")
        st.plotly_chart(figure2)

        with c2:
            total_cities = df.groupby("City")["Total Revenue"].sum().reset_index().nlargest(10,["Total Revenue"])
            # figure3 = px.treemap(data_frame = df, path = ["City"], values = "Total Revenue")
            figure3 = px.treemap(data_frame = total_cities, path = ["City"], values = "Total Revenue", title = "Top 10 Cities as per Total Revenue")
            st.plotly_chart(figure3)

            figure4 = px.pie(data_frame=df, names = "Offer", title = "Types of Offers")
            # figure4.update_layout(width = 400, height = 600)
            st.plotly_chart(figure4, use_container_width=True)

    with tab2:
        c1,c2 = st.columns(2)
        with c1:
            st.metric("📝Total Rows",df.shape[0])
        with c2:
            st.metric("🗒️Total Columns",df.shape[1])  
        c3,c4 = st.columns(2)
        with c3:
            # st.metric("❌Missing Values",0)
            st.metric("❌Missing Values",df.isna().sum().sum())
        with c4:
            st.metric("🔍Duplicate Rows",df.duplicated().sum())
        st.subheader("Dataset")
        st.dataframe(df)
        st.subheader("Column Names")
        # st.columns(df)
        st.dataframe(df.columns.tolist())
        # st.markdown(df.columns.tolist())

    with tab3:
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

if opt == "Customer Demographics & Services":
    d2.dashboard2()
       
if opt == "Churn Analysis":
    d3.dashboard3()

if opt == "Revenue & Customer Lifetime Value":
    d4.dashboard4()

if opt == "About":
    ab.about()