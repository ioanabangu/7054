<strong>FixTrack: IT Issue Reporting and Tracking System</strong>

<strong>Project Overview</strong>

<strong>FixTrack</strong> is a web-based IT issue reporting and tracking system developed as part of the Advanced Software Development and Framework module. The system allows users to submit, track, and manage IT-related hardware or software issues through a simple and intuitive interface. Users can report new issues, edit details, and mark them as resolved, with all changes reflected in the database in real-time.

The project incorporates Bootstrap for a responsive front-end design and uses Python with Flask for the back-end, connected to a MySQL database for data management.

<strong>Features</strong>
<ul>
  <li><strong>Issue Submission</strong>: Users can submit IT issues (hardware or software) with details such as project name, email, date, issue type, and a description.</li>
    <li><strong>Issue Tracking</strong>: Issues are stored in a MySQL database and displayed in a table format. Users can view all issues on the platform.</li>
    <li><strong>Edit and Delete Issues</strong>: Users can edit details of previously submitted issues or delete them entirely.</li>
    <li><strong>Responsive Design</strong>: Built using Bootstrap, the interface is mobile-friendly and responsive.</li>
    <li><strong>Real-Time Updates</strong>: Any additions, edits, or deletions are reflected immediately in the database and on the screen.</li>
</ul>

<strong>Technologies Used</strong>
<ul>
  <li>Front-End: HTML, CSS (Bootstrap framework), Responsive design for enhanced user experience</li>
  <li>Back-End: Python (Flask framework), MySQL for database management</li>
  <li>API: Integration with external email validation API to ensure correct email input.</li>
</ul>

<strong>Getting Started</strong>

<strong>Prerequisites</strong>

To run this project locally, you'll need:
<ul>
  <li>Python 3.x</li>
  <li>Flask</li>
  <li>MySQL</li>
  <li>Bootstrap</li>
    <li>Any MySQL-compatible client (e.g., MySQL Workbench)</li>
</ul>

<strong>Installation</strong>
<ol>
  <li>Clone the repository</li>
    <li>Install the required dependencies</li>
    <li>Create a MySQL database.</li>
    <li>Import the provided SQL script to set up the required tables.</li>
  <li>Configure the database connection</li>
  <li>Run the Flask app</li>
  <li>Open your browser and visit</li>
</ol>


<strong>Features in Future Development</strong>
<ul>
  <li><strong>Email Notifications</strong>: Automatically send notifications to users when their issue status changes.</li>
    <li><strong>Anonymous Reporting</strong>: Allow users to submit issues anonymously for increased flexibility.</li>
    <li><strong>Improved Data Analytics</strong>: Provide insights into the most common types of issues and response times.</li>
    <li><strong>Automated Deletion of Old Issues</strong>: Automatically remove or archive issues after a certain period.</li>
</ul>

<strong>Testing</strong>
The project includes basic functionality testing. However, there are areas to improve and expand, including error handling and additional validation for form inputs.
