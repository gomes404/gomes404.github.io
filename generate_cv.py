from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Change header color to match website (dark blue)
        self.set_fill_color(25, 25, 112)  # Dark blue color (#191970)
        self.rect(0, 0, 210, 30, 'F')
        self.ln(10)  # Move below the blue bar
        self.set_font("Arial", "B", 24)  # Larger font for name
        self.set_text_color(255, 255, 255)  # White text
        self.cell(0, 10, "Ricardo Bruno Ribeiro Gomes", ln=True, align="C")
        self.set_font("Arial", "I", 16)
        self.cell(0, 5, "Software Developer", ln=True, align="C")
        self.ln(10)

    def footer(self):
        # Position cursor at 1.5 cm from bottom
        self.set_y(-15)
        # Set font
        self.set_font('Arial', 'I', 8)
        # Set text color to dark blue
        self.set_text_color(25, 25, 112)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')
        # Add a decorative line
        self.line(10, 282, 200, 282)

    def section_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_fill_color(25, 25, 112)  # Dark blue color (#191970)
        self.set_text_color(255, 255, 255)  # White text
        self.cell(0, 10, f" {title}", ln=True, fill=True)
        self.ln(5)

    def section_body(self, body):
        self.set_font("Arial", "", 11)
        self.set_text_color(0, 0, 0)  # Black text
        self.multi_cell(0, 5, body)
        self.ln(5)

def generate_cv():
    pdf = PDF()
    pdf.alias_nb_pages()  # Make sure this is called before adding any pages
    pdf.add_page()

    # Contact Info
    pdf.set_font("Arial", "", 11)  # Slightly larger font for contact info
    pdf.set_text_color(25, 25, 112)  # Dark blue text (#191970)
    contact_info = (
        "Email: ricardo.gomes14@outlook.com | Phone: +44 (0) 7437461123\n"
        "LinkedIn: www.linkedin.com/in/ricardogomes404 | GitHub: github.com/gomes404\n"
        "Portfolio: https://gomes404.github.io/"
    )
    pdf.multi_cell(0, 5, contact_info, align='C')
    pdf.ln(10)

    # Professional Summary
    pdf.section_title("Professional Summary")
    summary = (
        "Motivated and skilled Software Developer with hands-on experience in web development and game design "
        "Proficient in HTML, CSS, JavaScript, and Unreal Engine, with a growing understanding of C++ and C#. "
        "Strong ability to design and develop user-centric solutions, demonstrated through web-based projects and game development. "
        "Adept in version control using Git/GitHub and a solid understanding of responsive design and UI/UX principles. "
        "Seeking a software development role where I can contribute technical expertise to develop scalable and efficient applications."
    )
    pdf.section_body(summary)

    # Technical Skills
    pdf.section_title("Technical Skills")
    skills = (
        "- Programming Languages: JavaScript, C++, C#, Ruby\n"
        "- Web Development: HTML, CSS, Angular.js, Responsive Web Design\n"
        "- Game Development: Unreal Engine, Unity\n"
        "- Version Control: Git, GitHub\n"
        "- Tools: Visual Studio, Unity, Trello, JIRA\n"
        "- Methodologies: Agile, Scrum"
    )
    pdf.section_body(skills)

    # Education
    pdf.section_title("Education")
    education = (
        "Games Technology (BTEC Level 3) - Access Creative College, Sep 2018 - Aug 2019\n"
        "- Focus: Game Design, Programming for Games, 3D Modeling, and Animation\n"
        "- Key Skills: Game production, visual effects, audio integration, project management."
    )
    pdf.section_body(education)

    # Work Experience
    pdf.section_title("Work Experience")
    work_experience = (
        "Ramp Agent, DHL, Bristol\n"
        "March 2023 - Present\n"
        "- Collaborated with teams to ensure safety and efficiency, developing solutions to optimize workflows.\n\n"

        "On-Site Manager, FastUK Parcel (Self-Employed), Bristol\n"
        "April 2022 - February 2023\n"
        "- Analyzed performance data to enhance operational efficiency - similar skills used in debugging and optimizing software."
    )
    pdf.section_body(work_experience)

    # Add a page break here
    pdf.add_page()

    # Relevant Projects
    pdf.section_title("Relevant Projects")
    projects = (
        "- Portfolio Project 1: Web-Based Portfolio\n"
        "  - Technologies: HTML, CSS, JavaScript\n"
        "  - Designed and developed a fully responsive personal portfolio website. Demonstrated web development skills, including a blog section, and portfolio projects.\n"
        "  - Implemented responsive design for optimal viewing across devices.\n"
        
        "- Portfolio Project 2: Singleplayer Game Development\n"
        "  - Technologies: Unreal Engine\n"
        "  - Developed a simple singleplayer game using Unreal Engine.\n"
        "  - Integrated UI features, and game mechanics.\n"
    )
    pdf.section_body(projects)

    # Languages
    pdf.section_title("Languages")
    languages = (
        "- Portuguese (Native), English (Fluent), Spanish (Advanced), Italian (Basic)"
    )
    pdf.section_body(languages)

    # Save the file
    pdf_file = "Ricardo_Gomes_Software_Developer_CV.pdf"
    pdf.output(pdf_file)
    print(f"CV successfully generated and saved as {pdf_file}")

if __name__ == "__main__":
    generate_cv()

