from ydata_profiling import ProfileReport
from databases.supabase_conn import load_database_data


boetes_df = load_database_data("SELECT * FROM TENNIS.teams;")

# Basic profiling report
profile = ProfileReport(boetes_df, title="Tennis DB Analysis")
profile.to_file("data_profiling/tennisdb_report.html")
print("Report saved as tennisdb_report.html")