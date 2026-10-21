package com.workflow.service;

import com.workflow.model.CaseRequest;
import com.workflow.model.CaseResponse;
import java.util.ArrayList;
import java.util.List;
import org.springframework.stereotype.Service;

@Service
public class CaseRoutingService {
    public CaseResponse routeCase(CaseRequest request) {
        String summaryText = request.getIssueSummary().toLowerCase();
        String issueCategory;
        String routeTo;
        String priority;
        List<String> missingFields = new ArrayList<>();

        if (summaryText.contains("warranty") || summaryText.contains("guarantee")
                || summaryText.contains("policy") || summaryText.contains("coverage")
                || summaryText.contains("compliance")) {
            issueCategory = "policy_case";
            routeTo = "policy_team";
            priority = summaryText.contains("critical") || summaryText.contains("fails") ? "high" : "medium";
        } else if (summaryText.contains("battery") || summaryText.contains("engine") || summaryText.contains("electrical") || summaryText.contains("fails") || summaryText.contains("fault")) {
            issueCategory = "technical_issue";
            routeTo = "technical_support";
            priority = summaryText.contains("critical") || summaryText.contains("fails") ? "high" : "medium";
        } else if (summaryText.contains("part") || summaryText.contains("spare")
                || summaryText.contains("component") || summaryText.contains("replace")
                || summaryText.contains("item") || summaryText.contains("stock")) {
            issueCategory = "inventory_request";
            routeTo = "inventory_team";
            priority = "medium";
        } else {
            issueCategory = "service_request";
            routeTo = "service_desk";
            priority = "low";
        }

        if (request.getOrganizationName() == null || request.getOrganizationName().isBlank()) {
            missingFields.add("organizationName");
        }
        if (request.getRequesterName() == null || request.getRequesterName().isBlank()) {
            missingFields.add("requesterName");
        }
        if (request.getAssetName() == null || request.getAssetName().isBlank()) {
            missingFields.add("assetName");
        }
        if (request.getAssetId() == null || request.getAssetId().isBlank()) {
            missingFields.add("assetId");
        }

        String summary = String.format("%s request classified as '%s' with priority '%s'. Route to %s.",
                request.getRequesterName(), issueCategory, priority, routeTo);

        return new CaseResponse(1L, issueCategory, priority, routeTo, summary, 0.91, missingFields);
    }

    public List<CaseResponse> listCases() {
        return List.of(
                new CaseResponse(101L, "policy_case", "high", "policy_team", "Policy review request", 0.94, List.of()),
                new CaseResponse(102L, "technical_issue", "medium", "technical_support", "Technical issue investigation", 0.89, List.of())
        );
    }
}
