package com.workflow.model;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public class CaseRequest {
    @NotBlank
    @Size(min = 2)
    private String organizationName;

    @NotBlank
    @Size(min = 2)
    private String requesterName;

    @NotBlank
    @Size(min = 2)
    private String assetName;

    @NotBlank
    @Size(min = 5)
    private String assetId;

    @NotBlank
    @Size(min = 10)
    private String issueSummary;

    private String requestType = "service_request";

    public String getOrganizationName() {
        return organizationName;
    }

    public void setOrganizationName(String organizationName) {
        this.organizationName = organizationName;
    }

    public String getRequesterName() {
        return requesterName;
    }

    public void setRequesterName(String requesterName) {
        this.requesterName = requesterName;
    }

    public String getAssetName() {
        return assetName;
    }

    public void setAssetName(String assetName) {
        this.assetName = assetName;
    }

    public String getAssetId() {
        return assetId;
    }

    public void setAssetId(String assetId) {
        this.assetId = assetId;
    }

    public String getIssueSummary() {
        return issueSummary;
    }

    public void setIssueSummary(String issueSummary) {
        this.issueSummary = issueSummary;
    }

    public String getRequestType() {
        return requestType;
    }

    public void setRequestType(String requestType) {
        this.requestType = requestType;
    }
}
