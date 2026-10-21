package com.workflow;

import static org.assertj.core.api.Assertions.assertThat;

import com.workflow.model.CaseRequest;
import com.workflow.model.CaseResponse;
import com.workflow.service.CaseRoutingService;
import org.junit.jupiter.api.Test;

class CaseRoutingServiceTest {
    @Test
    void routeCase_shouldClassifyWarrantyRequest() {
        CaseRequest request = new CaseRequest();
        request.setOrganizationName("Example Service Center");
        request.setRequesterName("Anna Schneider");
        request.setAssetName("Example Asset A");
        request.setAssetId("ASSET-001");
        request.setIssueSummary("A critical integration fails after an update. Policy coverage review requested.");

        CaseRoutingService service = new CaseRoutingService();
        CaseResponse response = service.routeCase(request);

        assertThat(response.getIssueCategory()).isEqualTo("policy_case");
        assertThat(response.getRouteTo()).isEqualTo("policy_team");
        assertThat(response.getPriority()).isEqualTo("high");
    }

    @Test
    void routeCase_shouldHandlePartsRequests() {
        CaseRequest request = new CaseRequest();
        request.setOrganizationName("Example Service");
        request.setRequesterName("Lukas Weber");
        request.setAssetName("Example Asset B");
        request.setAssetId("ASSET-002");
        request.setIssueSummary("Customer needs a replacement component from current stock.");

        CaseRoutingService service = new CaseRoutingService();
        CaseResponse response = service.routeCase(request);

        assertThat(response.getIssueCategory()).isEqualTo("inventory_request");
        assertThat(response.getRouteTo()).isEqualTo("inventory_team");
    }
}
