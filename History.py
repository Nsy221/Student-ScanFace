import streamlit as st
import face_rec
from face_rec import retrieve_data
#from Home import face_rec
from datetime import datetime

def history():
    name = 'attendance:logs'
    def load_logs(name,end =-1):
        logs_list = face_rec.r.lrange(name, start=0,end=end) #extract all data from redis database
        return logs_list

    logs = load_logs(name=name)
    log_entries = []

    # Assuming log_entries is a list of dictionaries like the one you provided
    logs = load_logs(name=name)
    log_entries = []

    for log_entry in logs:
        try:
            log_str = log_entry.decode("utf-8")  # Decode bytes to string
            data = log_str.split('@')
            if len(data) == 3:
                name, role, timestamp_str = data
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
                log_dict = {'Name': name, 'Role': role, 'Timestamp': timestamp}
                log_entries.append(log_dict)
            else:
                st.warning(f"Invalid log entry format: {log_entry}")
        except Exception as e:
            st.warning(f"Error parsing log entry: {log_entry}. Error: {e}")

    # Get unique names from log_entries
    student_names = set(entry['Name'] for entry in log_entries if entry['Role'] == 'Student')

    # Let the user choose the name interactively
    selected_name = st.selectbox("Select a name:", list(student_names))

    # Filter log_entries for entries with the selected name
    filtered_log_entries = [log for log in log_entries if log ['Name'] == selected_name]

    # Display the filtered user history
    if filtered_log_entries:
        st.table(filtered_log_entries)
    else:
        st.warning(f"No entries found for {selected_name}")


if __name__ == "__main__":
    history()