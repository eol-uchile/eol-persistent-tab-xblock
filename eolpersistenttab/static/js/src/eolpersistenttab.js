/*
       _=,_
    o_/6 /#\
    \__ |##/
     ='|--\
       /   #'-.
       \#|_   _'-. /
        |/ \_( # |" 
       C/ ,--___/
*/

function EolPersistentTabXBlock(runtime, element, settings) {

    $(function ($) {
        var modal = document.getElementById("modal_" + settings.location);
        var btn = document.getElementById("btn_" + settings.location);
        var span = document.getElementById("close_" + settings.location);

        /* Open Modal */
        btn.onclick = function() {
            modal.style.display = "block";
        }

        /* Close modal */
        span.onclick = function() {
            modal.style.display = "none";
        }
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    });
}

