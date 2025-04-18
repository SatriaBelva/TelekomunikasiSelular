def hide_sidebar():
    css = """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }

    [data-testid="stSidebarCollapsedControl"] {
        display: none;
    }

    #MainMenu{
        display: none;
    }

    .stAppDeployButton{
        display: none;
    }
    </style>
    """
    return css

def landing_page_style() :
    css = """
    <style>
    /* Gradient background */
    .landing-container {
        background: linear-gradient(135deg, #f3f4f6, #e0f7fa);
        padding: 50px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-top: 100px;
    }

    .landing-title {
        font-size: 40px;
        font-weight: 700;
        color: #0d47a1;
    }

    .landing-subtitle {
        font-size: 18px;
        color: #333333;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    .login-button {
        background-color: #4285F4;
        color: white;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        box-shadow: 0 4px 14px rgba(66, 133, 244, 0.4);
        transition: background-color 0.3s ease;
    }

    .login-button:hover {
        background-color: #3367d6;
    }

    [data-testid="stSidebar"] {
        display: none;
    }

    [data-testid="stSidebarCollapsedControl"] {
        display: none;
    }

    #MainMenu{
        display: none;
    }

    .stAppDeployButton{
        display: none;
    }

    </style>

    <div class="landing-container">
        <div class="landing-title">👋 Selamat Datang di Aplikasi Internship</div>
        <div class="landing-subtitle">
            Eksplorasi data, visualisasi, dan manajemen proyek <br>
            dalam satu dashboard interaktif.
        </div>

    """
    return css