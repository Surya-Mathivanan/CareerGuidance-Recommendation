from flask import Flask, render_template, request

app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user inputs from the form
    grades = request.form.get('grades')
    interests = request.form.get('interests')
    goal = request.form.get('goal')
    preferred_study = request.form.get('preferred_study')
    
    # Placeholder for recommendation response
    recommendation = f"<p>Based on your grades ({grades}), interest in {interests}, and your goal to become a {goal}, here are some recommendations:</p>"
    recommendation += "<ul>"

    # Recommendations based on grades, interests, and goal
    if grades == "80-85":
        if interests.lower() == "math" and goal.lower() == "engineer":
            recommendation += "<li>Consider starting with courses in <b>B.Tech/B.E. in Tier 2/3 Colleges (Mechanical, Civil, Electrical, Electronics)</b> and <b>Diploma in Engineering (later transition to B.Tech)</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Algebra" target="_blank">B.Tech/B.E. in Tier 2/3 Colleges (Mechanical, Civil, Electrical, Electronics)</a> and <a href="https://en.wikipedia.org/wiki/Calculus" target="_blank">Diploma in Engineering (later transition to B.Tech)s</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.coursera.org" target="_blank">learn more</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'Calculus Made Easy', 'Algebra for Beginners'</li>"

        elif interests.lower() == "science" and goal.lower() == "scientist":
            recommendation += "<li>Focus on subjects like <b>B.Sc. in General Sciences (Physics, Chemistry, Biology, Mathematics)</b> and <b>B.Sc. Biotechnology, Environmental Science, or Nursing</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Physics" target="_blank">B.Sc. in General Sciences (Physics, Chemistry, Biology, Mathematics)</a> and <a href="https://en.wikipedia.org/wiki/Biology" target="_blank">B.Sc. Biotechnology, Environmental Science, or Nursing</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.edx.org" target="_blank">edX</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'Physics Fundamentals', 'Biology Concepts'</li>"

        elif interests.lower() == "art" and goal.lower() == "artist":
            recommendation += "<li>Dive into <b>Creative Design</b> and <b>Fine Arts</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Creative_design" target="_blank">Creative Design</a> and <a href="https://en.wikipedia.org/wiki/Fine_arts" target="_blank">Fine Arts</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.udemy.com" target="_blank">Udemy</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'The Art of Color', 'Creative Techniques'</li>"

    elif grades == "86-90":
        if interests.lower() == "math" and goal.lower() == "engineer":
            recommendation += "<li>Advanced studies in <b>B.Tech/B.E. in Tier 1/2 Colleges (Computer Science, IT, Electrical, Electronics, and Communication)</b> and <b>B.Tech in private universities with good placement records (VIT, SRM, etc.)</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Linear_algebra" target="_blank">Linear Algebra</a> and <a href="https://en.wikipedia.org/wiki/Mechanics" target="_blank">Mechanics</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.khanacademy.org" target="_blank">Khan Academy</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'Introduction to Mechanics', 'Advanced Linear Algebra'</li>"

        elif interests.lower() == "science" and goal.lower() == "scientist":
            recommendation += "<li>Deepen your knowledge in <b>B.Sc. in top colleges (Physics, Mathematics, Chemistry)</b> and <b>Integrated B.Sc.-M.Sc. programs in Tier 1/2 colleges</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Organic_chemistry" target="_blank">B.Sc. in top colleges (Physics, Mathematics, Chemistry)</a> and <a href="https://en.wikipedia.org/wiki/Astronomy" target="_blank">Integrated B.Sc.-M.Sc. programs in Tier 1/2 colleges</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.futurelearn.com" target="_blank">FutureLearn</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'Organic Chemistry Concepts', 'Introduction to Astronomy'</li>"

        elif interests.lower() == "art" and goal.lower() == "artist":
            recommendation += "<li>Explore <b>Digital Art</b> and <b>3D Animation</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Digital_art" target="_blank">Digital Art</a> and <a href="https://en.wikipedia.org/wiki/3D_animation" target="_blank">3D Animation</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.skillshare.com" target="_blank">Skillshare</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'Digital Art for Beginners', '3D Animation Techniques'</li>"

    elif grades == "91-95":
        if interests.lower() == "math" and goal.lower() == "engineer":
            recommendation += "<li>Pursue in-depth studies in <b>B.Tech/B.E. in NITs, IIITs, or Top State Engineering Colleges (Mechanical, CS, Electrical, AI)</b> and <b>Consider preparing for GATE for postgraduate opportunities.</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Differential_equations" target="_blank">Differential Equations</a> and <a href="https://en.wikipedia.org/wiki/Thermodynamics" target="_blank">Thermodynamics</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.edx.org" target="_blank">edX</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'Differential Equations Demystified', 'Thermodynamics for Engineers'</li>"

        elif interests.lower() == "science" and goal.lower() == "scientist":
            recommendation += "<li>Focus on <b>B.Sc. Research at IISc, IISERs, NISER, or in Top Universities</b> and <b>Integrated M.Sc. (5-year programs)</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Quantum_mechanics" target="_blank">B.Sc. Research at IISc, IISERs, NISER, or in Top Universities</a> and <a href="https://en.wikipedia.org/wiki/Microbiology" target="_blank">Integrated M.Sc. (5-year programs)</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.coursera.org" target="_blank">Coursera</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'Introduction to Quantum Mechanics', 'Microbiology for Beginners'</li>"

        elif interests.lower() == "art" and goal.lower() == "artist":
            recommendation += "<li>Explore <b>Advanced Painting Techniques</b> and <b>Graphic Design</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Painting" target="_blank">Painting</a> and <a href="https://en.wikipedia.org/wiki/Graphic_design" target="_blank">Graphic Design</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.creativelive.com" target="_blank">CreativeLive</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'Advanced Painting Techniques', 'Graphic Design Foundations'</li>"

    elif grades == "96-100":
        if interests.lower() == "math" and goal.lower() == "engineer":
            recommendation += "<li>Engage in specialized fields like <b>B.Tech in IITs or NITs (Computer Science, Aerospace, AI, Robotics)</b> and <b>Dual degree programs (B.Tech + M.Tech)</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Machine_learning" target="_blank">B.Tech in IITs or NITs (Computer Science, Aerospace, AI, Robotics)</a> and <a href="https://en.wikipedia.org/wiki/Control_system" target="_blank">Dual degree programs (B.Tech + M.Tech)</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.udacity.com" target="_blank">Udacity</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'Deep Learning with Python', 'Control Systems Engineering'</li>"

        elif interests.lower() == "science" and goal.lower() == "scientist":
            recommendation += "<li>Dive into <b>B.Math/B.Stat at ISI (Indian Statistical Institute)</b> and <b>B.Sc. in Research at IISc or IITs, IISERs</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Genomics" target="_blank">B.Math/B.Stat at ISI (Indian Statistical Institute)</a> and <a href="https://en.wikipedia.org/wiki/Astrophysics" target="_blank">B.Sc. in Research at IISc or IITs, IISERs</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.sciencedirect.com" target="_blank">ScienceDirect</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'Genomics: A Beginner’s Guide', 'Astrophysics for People in a Hurry'</li>"

        elif interests.lower() == "art" and goal.lower() == "artist":
            recommendation += "<li>Master <b>Art Theory</b> and <b>Contemporary Art Practices</b>.</li>"
            recommendation += '<li>Learn more about <a href="https://en.wikipedia.org/wiki/Art_theory" target="_blank">Art Theory</a> and <a href="https://en.wikipedia.org/wiki/Contemporary_art" target="_blank">Contemporary Art</a>.</li>'
            if preferred_study.lower() == "online":
                recommendation += '<li>Online Resource: <a href="https://www.masterclass.com" target="_blank">MasterClass</a></li>'
            else:
                recommendation += "<li>Recommended Books: 'Art Theory: A Very Short Introduction', 'Contemporary Art: 1989 to the Present'</li>"

    recommendation += "</ul>"
    return render_template('result.html', recommendation=recommendation)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
