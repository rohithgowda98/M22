<!DOCTYPE html>
<html>
 <head>
<link rel="stylesheet" type="text/css" href="static/styles/styles.css"></link>
<title></title>
</head>
<body>
<div id="header">
<p id="name">{{user_name}}</p>
         <p id="email">{{email_id}}</p></a>
         <p id="contact">{{contact_number}}</p>
     </div>
     <div class="left">
     </div>
     <div class="right">
            
            <h3>Educational Qualifications</h3>
            <table>
                <tr id="heading">
                    <td>Grade</td>
                    <td>School Name</td>
                    <td>Percentage</td>
                    <td>Year</td>
                </tr>
                <tr>
                    <td>{{grade}}</td>
                    <td>{{school_name}}</td>
                    <td>{{percentage}}</td>
                    <td>{{year}}</td>
                </tr>
                
            </table>
            <h3>Independent Course</h3>
            <p>
            <ul><li>{{independent_course}}</li></ul>
            </p>    
            <h3>Hobbies:</h3>
            <p>
            <ul>
                <li>{{hobbies}}</li>
			</ul>
            </p>
            <h3>Personal Information:</h3>
            <p>
            <ul>
                <li>
					DOB: {{dob}}
                </li>
				<li>Father Name: {{father_name}}</li>
				<li>Mother Name: {{mother_name}}</li>
			</ul>
            </p>
            <h3>Declaration</h3>
            <p>
            I hereby declare that the details furnished above are true and correct to the best of my knowledge and belief.</p>
     </div>
     <div id="footer"></div>
    </body>
</html>
