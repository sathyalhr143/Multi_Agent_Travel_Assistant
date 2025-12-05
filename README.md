# ✈️ Travel Multi Agent (BeeAI Framework)
A sophisticated travel planning application built using the BeeAI Framework. This project orchestrates multiple autonomous AI agents—each with a specific role (Destination Expert, Travel Meterologist, Cultural and Language expert)—to collaborate with a Travel Coordinater AI agent and generate detailed, constraint-aware travel itineraries for users

### Click this link below to experience the agent 👇

https://multiagenttravelassistant-sathyaraj.streamlit.app/

## 📖 Table of Contents
- Key Features

- How It Works

- Project Structure

- Prerequisites

- Installation

- Configuration

- Usage

- Future Roadmap

## 🌟 Key Features
- Multi-Agent Orchestration: Uses the BeeAI Framework's workflow engine to manage state and handoffs between different agents.

- Real-Time Data: Integrated with tools like DuckDuckGoTool, OpenMeteroTool and WikipediaTool, to fetch up-to-date flight prices, weather, and local culture and events.

- Constraint Validation: A dedicated Budget Agent ensures the proposed itinerary adheres to the user's financial limits.

- Memory Management: Agents maintain context throughout the planning process to ensure preferences (dietary, accessibility, budget, etc.) are respected in every step.

- Structured Output: Generates the final plan in a clean JSON format.

## ⚙️ How It Works
This system utilizes a Sequential Workflow pattern where agents pass the "Travel Plan State" to one another.

- User Input: The user provides a prompt (e.g., "Plan a 5-day trip to Tokyo for $2000").

- Travel Coordinater Agent: Analyzing the prompt to extract variables: Destination, Dates, Budget, Interests.

- Destination Agent: Uses Wikipedia tool and Think tool to think and find Top attractions matching interests.

- - Flight options.

- - Hotel availability.
 
- Meterologist Agent: Uses Weather tools like OpenMeteroTool() to retrive weather information of the location


- Language and culture Agent: Uses Wikipedia tool to retrive information about the languages they speak and the culture people have in the location, to help the user to have an better experience. 

- Final Output: A complete itinerary is presented to the user.

### 📥 Installation Guide

1. Clone the repository**
Open your terminal and run:
```bash
git clone https://github.com/sathyalhr143/travel_multi_agent_using_beeai_framework.git
cd travel_multi_agent_using_beeai_framework
```
2. Create an environment
```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies You can install the dependencies using the requirements.txt file or via the setup script.

Option A: Standard Install

```bash
pip install -r requirements.txt
```

Option B: Install in Editable Mode (Recommended for Developers) This allows you to edit the code and have changes apply immediately without reinstalling.

```bash
pip install -e .
```


4. Create a .env file in the root directory.

Add your API keys. Example:

```
OPENAI_API_KEY=your_api_key_here
BEEAI_API_KEY=your_beeai_key_here
```

### ▶️ How to Run

```bash
python steamlit_app_local.py
```


### 📂 Project Structure
- setup.py: Configuration for packaging the project, allowing it to be installed as a library.

- requirements.txt: List of external Python packages required to run the project.

- src/ or end_to_end_travel_multi_agent/: Contains the source code for the agents and tools.





### 🤝 Contributing
- Fork the Project

- Create your Feature Branch (git checkout -b feature/AmazingFeature)

- Commit your Changes (git commit -m 'Add some AmazingFeature')

- Push to the Branch (git push origin feature/AmazingFeature)

- Open a Pull Request

https://github.com/user-attachments/assets/68e75781-e717-4bdb-97f8-8aebdd7d922a
