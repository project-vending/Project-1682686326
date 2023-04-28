
import os

project_name = "time_series_analysis_dashboard"

# Create the directory structure
if not os.path.exists(project_name):
    os.mkdir(project_name)
    os.mkdir(os.path.join(project_name, "data"))
    os.mkdir(os.path.join(project_name, "dashboard"))
    os.mkdir(os.path.join(project_name, "utils"))

# Create empty files
with open(os.path.join(project_name, "data", "sensor_data.txt"), "w") as f:
    pass

with open(os.path.join(project_name, "data", "stock_market_data.txt"), "w") as f:
    pass

with open(os.path.join(project_name, "data", "social_media_data.txt"), "w") as f:
    pass

with open(os.path.join(project_name, "data", "website_traffic.txt"), "w") as f:
    pass

with open(os.path.join(project_name, "dashboard", "app.py"), "w") as f:
    pass

with open(os.path.join(project_name, "utils", "aws.py"), "w") as f:
    pass

print("File structure and empty files created successfully!")
