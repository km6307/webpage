 const subjectSelect = document.getElementById('subject');
    const semesterSelect = document.getElementById('semester');
    const facultySelect = document.getElementById('facultyName');
    const subjectPlaceholder = subjectSelect.options[0].cloneNode(true);
    const allSubjectOptions = Array.from(subjectSelect.options).slice(1).map(option => option.cloneNode(true));
    const semesterThreeSubjects = ['DSA', 'Computer Network', 'OS', 'DBMS', 'WT'];
    const semesterFourSubjects = ['DS using C', 'CSO', 'SE', 'py', 'e-gov'];
    const semesterFiveSubjects = ['MT', 'Java', 'IOT', 'AI and ML', 'IC', 'IS'];
    const semesterSixSubjects = ['E&SU', 'E'];
    const shashwatSubjects = ['Computer Network', 'Java', 'CSO', 'IC'];
    const rajeevSubjects = ['DSA', 'DS using C', 'OS'];
    const anshuSubjects = ['IS', 'AI and ML', 'e-gov', 'WT'];
    const sakshiSubjects = ['IOT', 'DBMS', 'SE'];

    function updateFaculty() {
        if (rajeevSubjects.includes(subjectSelect.value)) {
            facultySelect.value = 'Rajeev kumar c';
        } else if (shashwatSubjects.includes(subjectSelect.value)) {
            facultySelect.value = 'Shashwat Srivastava';
        } else if (anshuSubjects.includes(subjectSelect.value)) {
            facultySelect.value = 'Anshu Singh';
        } else if (sakshiSubjects.includes(subjectSelect.value)) {
            facultySelect.value = 'sakshi yadav';
        } else if (subjectSelect.value === 'MT') {
            facultySelect.value = 'Vishal Negi';
        } else {
            facultySelect.value = '';
        }
    }

    function updateSubjects() {
        const selectedValue = subjectSelect.value;
        const semesterSubjects = {
            '3': semesterThreeSubjects,
            '4': semesterFourSubjects,
            '5': semesterFiveSubjects,
            '6': semesterSixSubjects
        };
        const availableSubjects = semesterSubjects[semesterSelect.value]
            ? allSubjectOptions.filter(option => semesterSubjects[semesterSelect.value].includes(option.value))
            : allSubjectOptions;

        subjectSelect.replaceChildren(subjectPlaceholder.cloneNode(true));
        availableSubjects.forEach(option => subjectSelect.add(option.cloneNode(true)));
        subjectSelect.value = availableSubjects.some(option => option.value === selectedValue)
            ? selectedValue
            : '';
        updateFaculty();
    }

    subjectSelect.addEventListener('change', updateFaculty);
    semesterSelect.addEventListener('change', updateSubjects);

    document.getElementById('feedbackForm').addEventListener('submit', function(event) {
        event.preventDefault();
        alert('Feedback submitted successfully!');
        // Here you can add code to send the form data to a server or process it as needed.
    });
