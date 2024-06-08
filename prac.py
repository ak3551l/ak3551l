<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Single Page</title>
        <style>
            div {
                display: none;
            }
        </style>

        <script>

            function showPage(page) {

                document.querySelectorAll('div').forEach(div => {
                    div.style.display = 'none';
                })
                document.querySelector(`#${page}`).style.display = 'block';
            }

            document.addEventListener('DOMContentLoaded', function() {
                document.querySelectorAll('button').forEach(button => {
                    button.onclick = function() {
                        showPage(this.dataset.page);
                    }
                })
            })

        </script>
    </head>
    <body>
        <button data-page="page1">Page 1</button>
        <button data-page="page2">Page 2</button>
        <button data-page="page3">Page 3</button>
        <div id="page1">
            <h1>This is Page 1.</h1>
        </div>
        <div id="page2">
            <h1>This is Page 2.</h1>
        </div>
        <div id="page3">
            <h1>This is Page 3.</h1>
        </div>
    </body>
</html>
