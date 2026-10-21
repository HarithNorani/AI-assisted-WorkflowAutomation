package com.bmw;

import static org.assertj.core.api.Assertions.assertThat;

import com.bmw.model.CaseRequest;
import com.bmw.model.CaseResponse;
import com.bmw.service.CaseRoutingService;
import org.junit.jupiter.api.Test;

class CaseRoutingServiceTest {
    @Test
    void routeCase_shouldClassifyWarrantyRequest() {
        CaseRequest request = new CaseRequest();
        request.setDealerName("Munich Motorrad Center");
        request.setCustomerName("Anna Schneider");
        request.setVehicleModel("R 1250 GS");
        request.setVin("WB10XXXX123456789");
        request.setIssueSummary("Battery keeps dying and engine fails to start. Warranty claim requested.");

        CaseRoutingService service = new CaseRoutingService();
        CaseResponse response = service.routeCase(request);

        assertThat(response.getIssueCategory()).isEqualTo("warranty_case");
        assertThat(response.getRouteTo()).isEqualTo("warranty_team");
        assertThat(response.getPriority()).isEqualTo("high");
    }

    @Test
    void routeCase_shouldHandlePartsRequests() {
        CaseRequest request = new CaseRequest();
        request.setDealerName("Berlin Motorrad");
        request.setCustomerName("Lukas Weber");
        request.setVehicleModel("K 1600 GT");
        request.setVin("WB11YYYY987654321");
        request.setIssueSummary("Customer needs replacement front brake pad and rotor.");

        CaseRoutingService service = new CaseRoutingService();
        CaseResponse response = service.routeCase(request);

        assertThat(response.getIssueCategory()).isEqualTo("parts_request");
        assertThat(response.getRouteTo()).isEqualTo("parts_desk");
    }
}
