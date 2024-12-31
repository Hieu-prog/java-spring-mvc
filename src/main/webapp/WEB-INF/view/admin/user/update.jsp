<%@page contentType="text/html" pageEncoding="UTF-8" %>
    <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
        <%@taglib uri="http://www.springframework.org/tags/form" prefix="form" %>

            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Update Users</title>

                <!-- Latest compiled and minified CSS -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
                <!-- Latest compiled JavaScript -->
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
                <!-- <link rel="stylesheet" href="/css/demo.css"> -->

                <script>
                    $(document).ready(() => {
                        const avatarFile = $("#avatarFile");
                        avatarFile.change(function (e) {
                            const imgURL = URL.createObjectURL(e.target.files[0]);
                            $("#avatarPreview").attr("src", imgURL);
                            $("#avatarPreview").css({ "display": "block" });
                        });
                    });
                </script>
                <script src="https://use.fontawesome.com/releases/v6.3.0/js/all.js" crossorigin="anonymous"></script>


            </head>

            <body>
                <div class="container mt-5">
                    <div class="row">
                        <div class="col-md-6 col-12 mx-auto">
                            <h3>Update a user </h3>
                            <hr />
                            <form:form method="post" action="/admin/user/create" modelAttribute="newUser" class="row"
                                enctype="multipart/form-data">
                                <div class="mb-3" style="display: none;">
                                    <label class="form-label">Id:</label>
                                    <form:input type="text" class="form-control" path="id" />
                                </div>
                                <input type="hidden" name="email" value="${newUser.email}" />
                                <div class="mb-3 col-12 col-md-6">
                                    <label class="form-label">Email:</label>
                                    <form:input type="email" class="form-control" path="email" disabled="true" />
                                </div>
                                <div class="mb-3 col-12 col-md-6">
                                    <label class="form-label">Password:</label>
                                    <form:input type="password" class="form-control" path="password" />
                                </div>
                                <div class="mb-3 col-12 col-md-6">
                                    <label class="form-label">Phone number:</label>
                                    <form:input type="text" class="form-control" path="phone" />
                                </div>
                                <div class="mb-3 col-12 col-md-6">
                                    <label class="form-label">Full Name:</label>
                                    <form:input type="text" class="form-control" path="fullName" />
                                </div>
                                <div class="mb-3 col-12">
                                    <label class="form-label">Address:</label>
                                    <form:input type="text" class="form-control" path="address" />
                                </div>

                                <div class="mb-3 col-12 col-md-6">
                                    <label class="form-label">Role:</label>
                                    <form:select class="form-select" path="role.name">
                                        <form:option value="ADMIN">ADMIN</form:option>
                                        <form:option value="USER">USER</form:option>
                                    </form:select>
                                </div>
                                <div class="mb-3 col-12 col-md-6">
                                    <label for="avatarFile" class="form-label">Avatar:</label>
                                    <input class="form-control" type="file" id="avatarFile" accept=".png, .jpg, .jpeg"
                                        name="hoidanitFile" />
                                </div>
                                <div class="col-12 mb-3">
                                    <img style="max-height: 250px; display: none;" alt="avatar preview"
                                        id="avatarPreview" />
                                </div>
                                <div class="col-12 mb-5">
                                    <button type="submit" class="btn btn-primary">Create</button>
                                </div>
                            </form:form>

                        </div>
                    </div>
                </div>
            </body>

            </html>