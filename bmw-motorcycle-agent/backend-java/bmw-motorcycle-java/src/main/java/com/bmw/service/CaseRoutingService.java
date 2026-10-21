package com.bmw.service;

import com.bmw.model.CaseRequest;
import com.bmw.model.CaseResponse;
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

        if (summaryText.contains("warranty") || summaryText.contains("guarantee")) {
            issueCategory = "warranty_case";
            routeTo = "warranty_team";
            priority = summaryText.contains("critical") || summaryText.contains("fails") ? "high" : "medium";
        } else if (summaryText.contains("battery") || summaryText.contains("engine") || summaryText.contains("electrical") || summaryText.contains("fails") || summaryText.contains("fault")) {
            issueCategory = "technical_fault";
            routeTo = "technical_support";
            priority = summaryText.contains("critical") || summaryText.contains("fails") ? "high" : "medium";
        } else if (summaryText.contains("part") || summaryText.contains("rotor") || summaryText.contains("brake") || summaryText.contains("pad")) {
            issueCategory = "parts_request";
            routeTo = "parts_desk";
            priority = "medium";
        } else {
            issueCategory = "service_request";
            routeTo = "service_desk";
            priority = "low";
        }

        if (request.getDealerName() == null || request.getDealerName().isBlank()) {
            missingFields.add("dealerName");
        }
        if (request.getCustomerName() == null || request.getCustomerName().isBlank()) {
            missingFields.add("customerName");
        }
        if (request.getVehicleModel() == null || request.getVehicleModel().isBlank()) {
            missingFields.add("vehicleModel");
        }
        if (request.getVin() == null || request.getVin().isBlank()) {
            missingFields.add("vin");
        }

        String summary = String.format("%s request classified as '%s' with priority '%s'. Route to %s.",
                request.getCustomerName(), issueCategory, priority, routeTo);

        return new CaseResponse(1L, issueCategory, priority, routeTo, summary, 0.91, missingFields);
    }

    public List<CaseResponse> listCases() {
        return List.of(
                new CaseResponse(101L, "warranty_case", "high", "warranty_team", "Customer warranty request", 0.94, List.of()),
                new CaseResponse(102L, "technical_fault", "medium", "technical_support", "Battery fault investigation", 0.89, List.of())
        );
    }
}
