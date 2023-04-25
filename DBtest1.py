import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.basedatatypes import BaseFigure
import streamlit_option_menu as option_menu

st.set_page_config(page_title="Enviboard", page_icon=":bar_chart:", layout="wide")


with open("css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True) 


#@st.cache
def read_file():
    df = pd.read_excel('Rough_data.xlsx', '8 Days - 3 times',
                        skiprows=2)
    return df


#function for charts style
def charts_style(form,df):
    if form=='Bar':
        df.update_layout(legend=dict(orientation="v"))
        df.update_xaxes(title_text='')
        df.update_yaxes(title_text='')
        df.update_xaxes(title_font=dict(size=3))
        df.update_xaxes(tickfont=dict(size=12))
        df.update_yaxes(tickfont=dict(size=12))
        df.update_layout(coloraxis_showscale=False)
        df.update_xaxes(ticklen=0)
        df.update_yaxes(ticklen=0)
        df.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0,0,0,0)')
        return df

#functions for charts
def df_to_chart(form,df,x_axis,y_axis,barmode,template,color,hover_data,orientation,title):
    width=500
    height=300
    text_auto='.2s'
    template='none'
    #'plotly_white'   
    #hover_data=['Legal Name', 'ISIN','Quartile', 'Rolling_Return', 'Standard Deviation', 'Annual Return', 'SIP Return', 'Sharpe Ratio', 'Alpha', 'Beta', 'Morningstar_Category']
    barmode='group'
    text_auto='.2s'
    if form=='Bar':    
        styled_df = px.bar(df, y=y_axis, x=x_axis,barmode=barmode,template=template,text_auto='.2s',color=color,hover_data=hover_data,orientation=orientation,title=title,height=300)
        styled_df_final=charts_style('Bar',styled_df)
        return styled_df_final

def figures(dataframe,):
    
    fig1 =px.bar(data_frame=dataframe, x='Day', y=['Temperature', 'Humidity', 'Moisture', 'pH', 'Gas', 'Pressure'],
        facet_col='Time (in 24 hr format)', barmode='group', 
        base='Time (in 24 hr format)',width=1050,height=500, 
        title='BarPlot over Three readings of All Days', template='none')
    fig1.update_layout(legend=None) 
    fig1.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0,0,0,0)')
    
    return fig1


st.sidebar.title("🌏 ENVIBOARD")

df=read_file()


with st.sidebar:
    menu=st.selectbox("📁 Menu",options=["Dashboard","Analysis","Report"])

if menu=="Dashboard":
    st.title("📈 Dashboard")
    chart_type=st.sidebar.radio("Select chart type",options=["Bar","Line"],horizontal=True)
    params=st.sidebar.multiselect("Select Parameters",options=['Temperature', 'Humidity', 'Moisture', 'pH', 'Gas', 'Pressure'],default=['Temperature', 'Humidity', 'Moisture', 'pH', 'Gas', 'Pressure'])
    
    if chart_type=="Bar":
        st.subheader("BarPlot over Three readings of All Days")
        fig =px.bar(data_frame=df, x='Day', y=params,
            facet_col='Time (in 24 hr format)', barmode='group', 
            base='Time (in 24 hr format)',width=1050,height=475, 
            template='none')
        fig.update_traces(showlegend=False)
        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0,0,0,0)')

        st.plotly_chart(fig)   

    elif chart_type=="Line":
        st.subheader("LinePlot over Three readings of All Days")
        fig=px.line(data_frame=df, x='Day',y=params,
        facet_col='Time (in 24 hr format)',width=1050,height=500) 
        fig.update_traces(showlegend=False)
        fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig)   

if menu=="Analysis":
    st.title("🔍 Analysis") 
    tab1,tab2=st.tabs(tabs=["📆 On Days","📅 Over Days"])
    with tab1:

        df_day1=df[0:3]
        df_day2=df[3:6]
        df_day3=df[6:9]
        df_day4=df[9:12]
        df_day5=df[12:15]
        df_day6=df[15:18]
        df_day7=df[18:21]
        df_day8=df[21:24]

        day=st.sidebar.selectbox("Select Day",options=['Day 1','Day 2','Day 3','Day 4','Day 5','Day 6','Day 7','Day 8'])
        params_2=st.sidebar.multiselect("Select Parameters",options=['Temperature', 'Humidity', 'Moisture', 'pH', 'Gas', 'Pressure'],default=['Temperature', 'Humidity', 'Moisture', 'pH', 'Gas', 'Pressure'])

        #chart_type=st.sidebar.radio("Chart type",options=["Bar","Line"],horizontal=True)
        def fig(df_day,param):
            #if chart_type=="Bar":
                fig =px.bar(data_frame=df_day, x='Day', y=param,
                barmode='group',base='Time (in 24 hr format)',facet_col='Time (in 24 hr format)',width=1050,height=400)
                fig.update_traces(showlegend=False)
                fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0,0,0,0)')
                return fig
    
        if day=='Day 1':
            st.subheader("All Parameters on 1st Day")
            st.plotly_chart(fig(df_day=df_day1,param=params_2))
        if day=='Day 2':
            st.subheader("All Parameters on 2nd Day")
            st.plotly_chart(fig(df_day=df_day2,param=params_2))
        if day=='Day 3':
            st.subheader("All Parameters on 3rd Day")
            st.plotly_chart(fig(df_day=df_day3,param=params_2))
        if day=='Day 4':
            st.subheader("All Parameters on 4th Day")
            st.plotly_chart(fig(df_day=df_day4,param=params_2))
        if day=='Day 5':
            st.subheader("All Parameters on 5th Day")
            st.plotly_chart(fig(df_day=df_day5,param=params_2))
        if day=='Day 6':
            st.subheader("All Parameters on 6th Day")
            st.plotly_chart(fig(df_day=df_day6,param=params_2))
        if day=='Day 7':
            st.subheader("All Parameters on 7th Day")
            st.plotly_chart(fig(df_day=df_day7,param=params_2)) 
        if day=='Day 8':
            st.subheader("All Parameters on 8th Day")
            st.plotly_chart(fig(df_day=df_day8,param=params_2))      
    
    with tab2:
        col=st.columns((2,1))
        parameter=col[1].selectbox("Select Parameter",options=['Temperature', 'Humidity', 'Moisture', 'pH', 'Gas', 'Pressure'])

        def fig2(dataframe,parameter):
            from plotly.basedatatypes import BaseFigure
            fig=px.line(data_frame=dataframe,x='Day',y=parameter,line_group='Time (in 24 hr format)',
                        color='Time (in 24 hr format)',text=parameter,height=375,width=1050)
            fig.update_traces(showlegend=False)
            fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0,0,0,0)')
            return fig
        col[0].subheader(str(parameter)+" over days")

        st.plotly_chart(fig2(df,parameter))

if menu=="Report":
    st.title("📋 Report")

    avg_temp=int(df['Temperature'].sum()/len(df['Temperature']))
    avg_humi=int(df['Humidity'].sum()/len(df['Humidity']))
    avg_moist=int(df['Moisture'].sum()/len(df['Moisture']))
    avg_ph=int(df['pH'].sum()/len(df['pH']))
    avg_gas=int(df['Gas'].sum()/len(df['Gas']))
    avg_pressure=int(df['Pressure'].sum()/len(df['Pressure']))

    st.subheader("💡 Avergare messures of parameters")
    col2 = st.columns((1,1,1,1,1,1))
    col2[0].metric("Temperature avg.",avg_temp)
    col2[1].metric("Humidity avg.", avg_humi)
    col2[2].metric("Moisture avg.", avg_moist)
    col2[3].metric("pH avg.", avg_ph)
    col2[4].metric("Gas avg.", avg_gas)
    col2[5].metric("Pressure avg.",avg_pressure)  

    st.subheader(" 📂 File")  
    st._legacy_dataframe(df.style.highlight_max(),height=1000)


