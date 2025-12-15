import streamlit as st
import pandas as pd
import io

st.title("📄 Text to Excel Converter")

# Upload TXT file
uploaded_file = st.file_uploader("Upload a Text/CSV file", type=["txt","csv"])

# Inputs
delimiter = st.text_input("Enter delimiter used in TXT file", value="|")

if uploaded_file:
    try:
        # Read TXT into DataFrame
        df = pd.read_csv(uploaded_file, delimiter=delimiter)

        # Preview DataFrame
        st.subheader("🔍 Preview")
        st.dataframe(df)

        # Convert to Excel
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Sheet1")
        excel_data = excel_buffer.getvalue()

        st.download_button(
            label="📥 Download Excel",
            data=excel_data,
            file_name=uploaded_file.name.rsplit(".", 1)[0] + ".xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        st.success("File converted successfully!")

    except Exception as e:
        st.error(f"❌ Error: {e}")
