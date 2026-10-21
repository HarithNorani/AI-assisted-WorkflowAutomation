package com.bmw.model;

import java.util.List;

public class CaseResponse {
    private Long caseId;
    private String issueCategory;
    private String priority;
    private String routeTo;
    private String summary;
    private Double confidence;
    private List<String> missingFields;

    public CaseResponse() {
    }

    public CaseResponse(Long caseId, String issueCategory, String priority, String routeTo, String summary,
                       Double confidence, List<String> missingFields) {
        this.caseId = caseId;
        this.issueCategory = issueCategory;
        this.priority = priority;
        this.routeTo = routeTo;
        this.summary = summary;
        this.confidence = confidence;
        this.missingFields = missingFields;
    }

    public Long getCaseId() {
        return caseId;
    }

    public void setCaseId(Long caseId) {
        this.caseId = caseId;
    }

    public String getIssueCategory() {
        return issueCategory;
    }

    public void setIssueCategory(String issueCategory) {
        this.issueCategory = issueCategory;
    }

    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }

    public String getRouteTo() {
        return routeTo;
    }

    public void setRouteTo(String routeTo) {
        this.routeTo = routeTo;
    }

    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }

    public Double getConfidence() {
        return confidence;
    }

    public void setConfidence(Double confidence) {
        this.confidence = confidence;
    }

    public List<String> getMissingFields() {
        return missingFields;
    }

    public void setMissingFields(List<String> missingFields) {
        this.missingFields = missingFields;
    }
}
