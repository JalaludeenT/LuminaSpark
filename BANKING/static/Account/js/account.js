$(document).ready(function () {
        // Function to populate branches based on the selected district
        function populateBranches() {
            var districtId = $('#district').val();
            $.ajax({
                url: '{% url "BANK:get_branches" %}',
                data: { 'district': districtId },
                dataType: 'json',
                success: function (data) {
                    var branchesSelect = $('#branch');
                    branchesSelect.empty(); // Clear existing options
                    $.each(data.branches, function (index, branch) {
                        branchesSelect.append($('<option>', {
                            value: branch.id,
                            text: branch.name
                        }));
                    });
                }
            });
        }

        // Attach the function to the change event of the district dropdown
        $('#district').change(function () {
            populateBranches();
        });

        // Call the function on page load if a district is already selected
        populateBranches();
    });
//*************************************************************************************************************//

        $(document).ready(function () {
            // Store the initial state of the 'Nothing Want to select' checkbox
            var selectAnyOneCheckbox = $('#id_materials_provide_0');
            var selectAnyOneChecked = selectAnyOneCheckbox.prop('checked');

            // Add a change event listener to the 'Nothing Want' checkbox
            selectAnyOneCheckbox.change(function () {
                if ($(this).prop('checked')) {
                    // If 'Nothing Want' is checked, uncheck other checkboxes and 'None'
                    $('input[name="materials_provide"]').not(this).prop('checked', false);
                    $('#id_uncheck_all').prop('checked', false);
                } else {
                    // If 'Select any one' is unchecked, restore the initial state of other checkboxes
                    $('input[name="materials_provide"]').not(this).prop('checked', selectAnyOneChecked);
                }
            });

            // Change event listener for 'None' checkbox
            $('#id_uncheck_all').change(function () {
                if ($(this).prop('checked')) {
                    // If 'None' is checked, None 'Materials Provide' checkboxes
                    $('input[name="materials_provide"]').prop('checked', false);
                }
            });

            // Change event listener for individual 'Materials Provide' checkboxes
            $('input[name="materials_provide"]').change(function () {
                // If any 'Materials Provide' checkbox is checked, uncheck 'None'
                if ($(this).prop('checked')) {
                    $('#id_uncheck_all').prop('checked', false);
                }
            });
        });
    });
//***************************************************************************************************************//


    // Function to check if the form is completely filled, including materials checkbox
    function isFormFilled() {
        var isFilled = true;

        // Check each input and select element in the form
        $('#accountForm input, #accountForm select').each(function () {
            // Ignore hidden elements
            if ($(this).is(':hidden')) {
                return true; // Continue to the next iteration
            }

            // Check if the field is empty
            if ($(this).val() === '') {
                isFilled = false;
                return false; // Break the loop if any field is empty
            }
        });

        // Check if at least one materials checkbox is checked
        if ($('input[name="materials_provide"]:checked').length === 0) {
            isFilled = false;
        }

        return isFilled;
    };

//*****************************************************************************************************************//

    // Initially hide the second container
    $('.container.clr').hide();

    // Variable to track form submission status
    var formSubmitted = false;

    // Function to show the second container and hide the first container
    function toggleContainers() {
        if (isFormFilled()) {
            $('.container').hide();
            $('.container.clr').show();
            formSubmitted = true; // Set form submission status to true
            return false; // Prevent form submission
        } else {
            alert('Please fill in all the fields');
            formSubmitted = false; // Set form submission status to false
            return false; // Prevent form submission
        }
    }

    // Function to show the first container and hide the second container
    function showFirstContainer() {
    // Always show the first container and hide the second container
    $('.container.clr').hide();
    $('.container').show();
  }
</script>


<script>
$(document).ready(function () {
    // Check if created_account_id is available in the context
    var createdAccountId = {{ created_account_id|default:"null" }};

    // If created_account_id is available and not empty, show the button
    if (createdAccountId !== null && createdAccountId !== "") {
        $(".button2").show();

        // Attach click event to the button to redirect to account_details_view
        $(".button2 button").click(function () {
            var redirectUrl = "{% url 'BANK:account_details_view' user_id=user_id account_id=createdAccountId %}";
            window.location.href = redirectUrl;
        });
    }
});
</script>