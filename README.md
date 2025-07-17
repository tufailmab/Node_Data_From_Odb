</head>
<body>
  <h1>Node Data From ODB</h1>

  <p>
    This Python script extracts node labels and coordinates from an Abaqus <code>.odb</code> file and saves the data in a readable text file. Developed initially out of curiosity, it simplifies node geometry extraction for FEA post-processing workflows.
  </p>

  <h2>Features</h2>
  <ul>
    <li><strong>Automatic ODB Detection:</strong> Finds and opens the first <code>.odb</code> file in the current directory.</li>
    <li><strong>Node Data Export:</strong> Extracts node label and coordinates (X, Y, Z) for each instance.</li>
    <li><strong>Clean Formatting:</strong> Saves organized node data into a human-readable text file.</li>
    <li><strong>Skips Main Assembly:</strong> Ignores top-level "ASSEMBLY" instance for cleaner output.</li>
  </ul>

  <h2>Usage Instructions</h2>
  <ol>
    <li>Place this script in the same directory as your Abaqus <code>.odb</code> file.</li>
    <li>Run the script using Abaqus CAE:
      <pre><code>abaqus cae noGUI=node_data_from_odb.py</code></pre>
    </li>
    <li>The extracted node information will be saved to <code>node_data.txt</code> in the same directory.</li>
  </ol>

  <h2>Requirements</h2>
  <p>This script requires the following:</p>
  <ul>
    <li>Abaqus CAE (for accessing Abaqus Python API)</li>
    <li>Python 2.7 (used by Abaqus internally)</li>
    <li><code>win32com</code> and <code>subprocess</code> (optional, included for Excel control)</li>
  </ul>

  <h2>License</h2>
  <p>This project is licensed under the <strong>MIT License</strong>.</p>
  <p>You are free to use, modify, and distribute this software under the terms of the MIT License. Please give credit if used in publications or shared work.</p>

  <h2>Developer Information</h2>
  <ul>
    <li><strong>Developer:</strong> Engr. Tufail Mabood</li>
    <li><strong>Contact:</strong> <a href="https://wa.me/+923440907874">WhatsApp</a></li>
    <li><strong>Note:</strong> This tool was developed out of curiosity and is shared as an open-source utility. Contributions are welcome.</li>
  </ul>
</body>
</html>
