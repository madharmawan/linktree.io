from Node import Node


def update(nodes):
    """Update the website. By writing the HTML"""
    write_html(nodes)
    refresh()
    return


def write_html(nodes):
    """Creates the HTML necessary and writes it to a file."""
    f = open('tester.html', 'w')
    
    setup = setup_message()
    body = setup_body()
    node_html = ""
    for node in nodes:
        node_html += write_node(node)
    closing = end_html()


    message = setup + body + node_html + closing
    f.write(message)
    f.close()

    
def setup_message():
    """Creates all the node links"""
    return """<!DOCTYPE html>
<html>
    <head>
        <title>W3.CSS Template</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
            body,
            h1,
            h2,
            h3,
            h4,
            h5,
            h6 {
                font-family: "Lato", sans-serif;
            }

            body,
            html {
                height: 100%;
                color: #777;
                line-height: 1.8;
            }

            /* Create a Parallax Effect */
            .bgimg-1,
            .bgimg-2,
            .bgimg-3 {
                background-attachment: fixed;
                background-position: center;
                background-repeat: no-repeat;
                background-size: cover;
            }

            /* First image (Logo. Full height) */
            .bgimg-1 {
                background-image: url('https://www.w3schools.com/w3images/parallax1.jpg');
                min-height: 100%;
            }

            /* Second image (Portfolio) */
            .bgimg-2 {
                background-image: url("https://www.w3schools.com/w3images/parallax2.jpg");
                min-height: 400px;
            }

            /* Third image (Contact) */
            .bgimg-3 {
                background-image: url("https://www.w3schools.com/w3images/parallax3.jpg");
                min-height: 400px;
            }

            .w3-wide {
                letter-spacing: 10px;
            }

            .w3-hover-opacity {
                cursor: pointer;
            }

            /* Turn off parallax scrolling for tablets and phones */
            @media only screen and (max-device-width: 1600px) {

                .bgimg-1,
                .bgimg-2,
                .bgimg-3 {
                    background-attachment: scroll;
                    min-height: 400px;
                }
            }
        </style>
    </head>
<body>

    

    <!-- First Parallax Image with Logo Text -->
    <div class="bgimg-1 w3-display-container w3-opacity-min" id="home">
        <div class="w3-display-middle" style="white-space:nowrap;">
            <span class="w3-center w3-padding-large w3-black w3-xlarge w3-wide w3-animate-opacity">NEWMAN <span
                    class="w3-hide-small">EVENTS
        </div>
    </div>"""


def setup_body():
    """Sets up the body correctly with HTML."""
    return """<div class="w3-content w3-container w3-padding-64" id="about">"""

def write_node(node: Node):
    """Returns a string of the node necessary."""
    node_info = node.display_node()
    node_title = node_info[0]
    node_description = node_info[1]
    node_contact = node_info[2]
    node_link = node_info[3]
    node_image = node_info[4]

    ret_string = f"""<h5 class="w3-center">{node_title}</h5>
    <p>{node_description}<br><br>"""

    if node_contact:
        ret_string += f"""Contact: {node_contact}<br><br>"""
    if node_link:
        ret_string += f"""Link: {node_link}\n\n"""
    
    ret_string += "</p>\n\n"
    return ret_string

def end_html():
    """Finishes the HTML program."""
    return """</div>

    <!-- Second Parallax Image with Portfolio Text -->
    <div class="bgimg-2 w3-display-container w3-opacity-min">
        <div class="w3-display-middle">
            <span class="w3-xxlarge w3-text-white w3-wide">PORTFOLIO</span>
        </div>
    </div>

    
    <!-- Modal for full size images on click-->
    <div id="modal01" class="w3-modal w3-black" onclick="this.style.display='none'">
        <span class="w3-button w3-large w3-black w3-display-topright" title="Close Modal Image"><i
                class="fa fa-remove"></i></span>
        <div class="w3-modal-content w3-animate-zoom w3-center w3-transparent w3-padding-64">
            <img id="img01" class="w3-image">
            <p id="caption" class="w3-opacity w3-large"></p>
        </div>
    </div>



    <script>
        // Modal Image Gallery
        function onClick(element) {
            document.getElementById("img01").src = element.src;
            document.getElementById("modal01").style.display = "block";
            var captionText = document.getElementById("caption");
            captionText.innerHTML = element.alt;
        }

        // Change style of navbar on scroll
        window.onscroll = function () { myFunction() };
        function myFunction() {
            var navbar = document.getElementById("myNavbar");
            if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
                navbar.className = "w3-bar" + " w3-card" + " w3-animate-top" + " w3-white";
            } else {
                navbar.className = navbar.className.replace(" w3-card w3-animate-top w3-white", "");
            }
        }

        // Used to toggle the menu on small screens when clicking on the menu button
        function toggleFunction() {
            var x = document.getElementById("navDemo");
            if (x.className.indexOf("w3-show") == -1) {
                x.className += " w3-show";
            } else {
                x.className = x.className.replace(" w3-show", "");
            }
        }
    </script>

</body>

</html>
    
    """

def refresh():
    """Refreshes the website."""

