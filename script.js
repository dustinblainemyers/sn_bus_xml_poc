(function executeRule(current, previous /*null when async*/ ) {

    // Example: Set the 'short_description' field of the current task
    current.short_description = "Updated by a business rule!";

})(current, previous);