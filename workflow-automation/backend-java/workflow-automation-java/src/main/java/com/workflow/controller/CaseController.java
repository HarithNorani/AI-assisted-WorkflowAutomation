package com.workflow.controller;

import com.workflow.model.CaseRequest;
import com.workflow.model.CaseResponse;
import com.workflow.service.CaseRoutingService;
import jakarta.validation.Valid;
import java.util.List;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1")
public class CaseController {
    private final CaseRoutingService caseRoutingService;

    public CaseController(CaseRoutingService caseRoutingService) {
        this.caseRoutingService = caseRoutingService;
    }

    @PostMapping("/cases/submit")
    public ResponseEntity<CaseResponse> submitCase(@Valid @RequestBody CaseRequest request) {
        CaseResponse response = caseRoutingService.routeCase(request);
        return ResponseEntity.ok(response);
    }

    @GetMapping("/cases")
    public ResponseEntity<List<CaseResponse>> listCases() {
        return ResponseEntity.ok(caseRoutingService.listCases());
    }
}
