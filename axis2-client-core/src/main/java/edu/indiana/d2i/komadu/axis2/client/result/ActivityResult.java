package edu.indiana.d2i.komadu.axis2.client.result;

import edu.indiana.d2i.komadu.axis2.client.ActivityType;

public class ActivityResult {

    private ActivityType activity;
    private String activityId;

    public void setActivity(ActivityType activity) {
        this.activity = activity;
    }

    public void setActivityId(String activityId) {
        this.activityId = activityId;
    }

    public ActivityType getActivity() {
        return activity;
    }

    public String getActivityId() {
        return activityId;
    }

}
