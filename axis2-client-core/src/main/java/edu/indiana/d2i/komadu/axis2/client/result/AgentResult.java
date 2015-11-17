package edu.indiana.d2i.komadu.axis2.client.result;

import edu.indiana.d2i.komadu.axis2.client.AgentType;
import edu.indiana.d2i.komadu.axis2.client.GenericAgentType;

public class AgentResult {

    private AgentType agent;
    private String agentId;

    public AgentType getAgent() {
        return agent;
    }

    public void setAgent(AgentType agent) {
        this.agent = agent;
    }

    public String getAgentId() {
        return agentId;
    }

    public void setAgentId(String agentId) {
        this.agentId = agentId;
    }

}
