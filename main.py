import os
import streamlit as st
import pandas as pd

# Đọc dữ liệu từ file Excel
@st.cache_data
def load_address_data():
    file_path = os.path.join('data', 'address_data.xls')
    return pd.read_excel(file_path)

# Load dữ liệu
df = load_address_data()

# Khởi tạo session state nếu chưa có
if 'province' not in st.session_state:
    st.session_state.province = ''
if 'district' not in st.session_state:
    st.session_state.district = ''
if 'ward' not in st.session_state:
    st.session_state.ward = ''

# Hàm cập nhật giá trị
def update_province():
    st.session_state.district = ''
    st.session_state.ward = ''

def update_district():
    st.session_state.ward = ''

# Tạo các dropdown cho tỉnh, huyện, xã
provinces = [''] + sorted(df['Tỉnh Thành Phố'].unique().tolist())
selected_province = st.selectbox('Chọn tỉnh/thành phố', provinces, key='province', on_change=update_province)

if selected_province:
    districts = [''] + sorted(df[df['Tỉnh Thành Phố'] == selected_province]['Quận Huyện'].unique().tolist())
    selected_district = st.selectbox('Chọn quận/huyện', districts, key='district', on_change=update_district)

    if selected_district:
        wards = [''] + sorted(df[(df['Tỉnh Thành Phố'] == selected_province) & (df['Quận Huyện'] == selected_district)]['Phường Xã'].unique().tolist())
        selected_ward = st.selectbox('Chọn phường/xã', wards, key='ward')

        if selected_ward:
            st.write(f'Bạn đã chọn: {selected_ward}, {selected_district}, {selected_province}')